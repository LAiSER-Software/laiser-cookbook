# Job Skill Analysis with LAiSER

This project provides a workflow for extracting and visualizing in-demand professional skills from job descriptions using the `laiser` library and Large Language Models (LLMs).

## Table of Contents

1. [Installation](#installation)
2. [Setup and Initialization](#setup-and-initialization)
3. [Data Loading](#data-loading)
4. [Skill Extraction](#skill-extraction)
5. [Visualization](#visualization)

## Installation

To run this project, install the required dependencies:

```bash
pip install laiser pandas matplotlib wordcloud torch
```

## Setup and Initialization

The project uses the `SkillExtractorRefactored` class. To initialize it, provide a model ID and the corresponding API key (for example, Gemini API).

```python
from laiser.skill_extractor_refactored import SkillExtractorRefactored

model_id = "gemini"
api_key = "YOUR_API_KEY"

se = SkillExtractorRefactored(model_id=model_id, api_key=api_key, use_gpu=False)
```

## Data Loading

The extractor expects a pandas DataFrame containing job descriptions. You can use your own CSV file or load the sample dataset:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/LAiSER-Software/datasets/refs/heads/master/jobs-data/linkedin_jobs_sample_36rows.csv"
job_postings = pd.read_csv(url)
job_postings = job_postings[["description", "job_id"]].dropna()
```

## Skill Extraction

Extract skills and align them to a standard format using `extract_and_align`:

```python
extracted_skills = se.extract_and_align(
	job_postings,
	id_column="job_id",
	text_columns=["description"],
	input_type="job_desc",
)
```

## Visualization

You can visualize the extracted skill landscape using:

- **Bar Chart**: Shows the top 20 most frequent skills.
- **Word Cloud**: Generates a cloud from raw extracted skills for a quick visual summary.

## Credits

- Created by Satya Phanindra Kumar Kalaga - September 2025
- Updated by Udit Chowdary Jasti - March 2026

