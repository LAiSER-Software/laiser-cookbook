"""Extract skills from a sample job description with LAiSER and print them.

Pick the AI model with LAISER_LLM (default: ollama):
  - ollama: a model in your local Ollama app; nothing leaves your Mac.
      Choose which one with OLLAMA_MODEL (default: gemma4), e.g.
      OLLAMA_MODEL=qwen3.6 python example.py
  - gemini: Google's Gemini API. Needs GEMINI_API_KEY.
  - local:  a small open model run by laiser itself on the CPU.
      The first run downloads it (about 3 GB) into ~/.cache/huggingface.

Usage:
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python extract_skills.py
"""

import os

import pandas as pd
import requests

from laiser import SkillExtractor

LOCAL_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4")

JOB_DESCRIPTION = """
Data Analyst, Office of Institutional Research

We are looking for a Data Analyst to turn university data into insight for
leadership. You will write SQL queries against our student information system,
build dashboards in Tableau, and clean and analyze large datasets in Python
(pandas). You will run statistical analyses such as regression and significance
testing, present findings to non-technical audiences, and document data
definitions. Experience with data governance, survey design, and FERPA
compliance is a plus. Strong written communication and project management
skills are required.
"""


def ollama_generate(prompt: str, temperature: float = 0.0, seed=42, **_ignored) -> str:
    """Send one prompt to the local Ollama server and return its reply text."""
    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "think": False,  # skip the hidden reasoning step on models that have one
            "options": {"temperature": temperature, "seed": seed},
        },
        timeout=600,
    )
    resp.raise_for_status()
    return resp.json()["response"]


def make_ollama_extractor() -> SkillExtractor:
    # laiser has no Ollama option. Starting it in Gemini mode makes it skip loading
    # a model of its own; every prompt then goes through router.generate, which we
    # point at Ollama, so no request is ever sent to Google.
    try:
        requests.get(f"{OLLAMA_URL}/api/version", timeout=3).raise_for_status()
    except requests.RequestException:
        raise SystemExit(f"Ollama isn't reachable at {OLLAMA_URL}. Open the Ollama app and try again.")
    extractor = SkillExtractor(model_id="gemini", api_key="unused")
    extractor.skill_service.router.generate = ollama_generate
    return extractor


def make_extractor() -> SkillExtractor:
    choice = os.getenv("LAISER_LLM", "ollama").lower()
    if choice == "ollama":
        print(f"Using Ollama model {OLLAMA_MODEL}")
        return make_ollama_extractor()
    if choice == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise SystemExit("Set GEMINI_API_KEY to use Gemini.")
        print("Using Gemini API")
        return SkillExtractor(model_id="gemini", api_key=api_key)
    print(f"Using local model {LOCAL_MODEL} on CPU")
    return SkillExtractor(model_id=LOCAL_MODEL, use_gpu=False)


def main() -> None:
    data = pd.DataFrame([{"Research ID": "job-1", "description": JOB_DESCRIPTION}])

    extractor = make_extractor()
    results = extractor.extract_concepts(
        data,
        id_column="Research ID",
        text_columns=["description"],
        input_type="job_desc",
        concepts=["skills"],  # or ["all"] for skills, knowledge and tasks
        top_k=10,
        output_csv_path="skills_output.csv",
    )

    if results is None or len(results) == 0:
        print("No skills found.")
        return

    cols = ["Raw Concept", "Taxonomy Concept", "Taxonomy Source", "Correlation Coefficient"]
    pd.set_option("display.width", 160)
    pd.set_option("display.max_colwidth", 50)
    print(results[[c for c in cols if c in results.columns]].to_string(index=False))
    print(f"\n{len(results)} rows saved to skills_output.csv")


if __name__ == "__main__":
    main()
