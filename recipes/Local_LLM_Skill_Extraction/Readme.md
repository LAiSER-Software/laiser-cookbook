# Skill Extraction with a Local LLM (Ollama)

Extract skills from a job description with LAiSER using a model that runs on your own computer through [Ollama](https://ollama.com), so the text never leaves your machine. The same script can also use the Gemini API or a small open model that LAiSER loads itself on the CPU.

## Narrative

Job descriptions, course outlines and HR records often can't be sent to a cloud API, because of privacy rules (FERPA, internal data policies) or simply cost. LAiSER doesn't ship an Ollama backend, but it routes every prompt through one function. This recipe swaps that function for a call to a local Ollama server, so you get LAiSER's skill extraction and taxonomy alignment (O*NET, UK Occupational Skills, and others) with no external API key and no data leaving your computer.

The sample input is a job posting for a Data Analyst in a university Office of Institutional Research. The script extracts the skills, aligns each to a taxonomy concept, prints a table and saves the results to `skills_output.csv`.

## Prerequisites

- Python 3.10 or newer
- One of these model backends:
  - **Ollama** (default): the [Ollama app](https://ollama.com/download) running locally with a model pulled, for example `ollama pull gemma4`
  - **Gemini**: a `GEMINI_API_KEY`
  - **Local**: nothing extra; the first run downloads `Qwen/Qwen2.5-1.5B-Instruct` (about 3 GB) into `~/.cache/huggingface`

## Setup

```bash
cd recipes/Local_LLM_Skill_Extraction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python extract_skills.py
```

Choose the backend and model with environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `LAISER_LLM` | `ollama` | `ollama`, `gemini`, or `local` |
| `OLLAMA_MODEL` | `gemma4` | Any model you've pulled into Ollama |
| `OLLAMA_HOST` | `http://localhost:11434` | Where the Ollama server is listening |
| `GEMINI_API_KEY` | none | Required when `LAISER_LLM=gemini` |

Examples:

```bash
OLLAMA_MODEL=qwen3.6 python extract_skills.py
LAISER_LLM=gemini GEMINI_API_KEY=your-key python extract_skills.py
LAISER_LLM=local python extract_skills.py
```

## How the Ollama hook works

`SkillExtractor` is created in Gemini mode with a placeholder key, which makes it skip loading a model of its own. The script then replaces `extractor.skill_service.router.generate` with `ollama_generate`, which posts each prompt to Ollama's `/api/generate` endpoint. No request is sent to Google.

This hook relies on LAiSER's internal attribute names, which is why `requirements.txt` pins `laiser==1.0.1`. If you upgrade LAiSER and the Ollama mode breaks, check that `skill_service.router.generate` still exists.

## Data

The job description is embedded in the script as `JOB_DESCRIPTION`. To run on your own data, replace the one-row DataFrame in `main()` with your own, for example:

```python
data = pd.read_csv("my_jobs.csv")  # needs an ID column and a text column
results = extractor.extract_concepts(
    data,
    id_column="job_id",
    text_columns=["description"],
    input_type="job_desc",
    concepts=["skills"],  # or ["all"] for skills, knowledge and tasks
)
```

`sample_output.csv` shows the result of one run with Ollama and `gemma4`, so you can see the expected columns without running a model. Results vary by model.

## Credits

- Created by [munnerley](https://github.com/munnerley) - November 2026
