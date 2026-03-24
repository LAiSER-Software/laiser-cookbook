# Pay Equity Analysis Using Skill Extraction

## Project Overview

This project provides an HR analytics framework to analyze compensation data based on actual skills extracted from job descriptions. By moving beyond simple job titles, organizations can ensure pay equity by aligning salaries with the technical and soft skills required for each role.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Author](#author)
6. [License](#license)

## Features

- **Automated Skill Extraction**: Uses the `laiser` library and generative AI (Gemini) to identify skills within unstructured job descriptions.
- **Taxonomy Alignment**: Maps extracted skills to standardized taxonomies like ESCO or O*NET.
- **Compensation Analysis**: Correlates the number and complexity of required skills with current salary levels.
- **Visualization**: Provides scatter plots to identify outliers where roles with similar skill sets have significant pay gaps.

## Prerequisites

Before running the analysis, ensure you have the following:

- Python 3.10+
- A Hugging Face API Token (for model access)
- A Gemini API Key (if using the Gemini model configuration)

## Installation

Install the required dependencies using pip:

```bash
pip install laiser pandas matplotlib seaborn torch
```

## Usage

### 1. Initialization

Initialize the `SkillExtractorRefactored` with your API credentials:

```python
from laiser.skill_extractor_refactored import SkillExtractorRefactored

se = SkillExtractorRefactored(model_id="gemini", api_key="YOUR_API_KEY")
```

### 2. Data Preparation

Prepare a CSV file or pandas DataFrame containing:

- `job_id`
- `job_title`
- `description`
- `salary`

### 3. Skill Extraction

Run the alignment tool to extract skills:

```python
extracted_skills = se.extract_and_align(
	job_data,
	id_column="job_id",
	text_columns=["description"],
)
```

### 4. Visualization

Analyze the results by plotting salary against the count of extracted skills to identify potential equity issues.

## Author

**Satya Phanindra Kumar Kalaga**  
**Udit Chowdary Jasti
Date: March 2026

## License

This project is for analytical purposes. Please ensure compliance with local data privacy and HR regulations regarding salary data.
