# University Program Skill Analysis with LAiSER

This project provides an automated workflow to extract and categorize professional skills from university program descriptions using the `laiser` library and Large Language Models (LLMs).

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Key Features](#key-features)
4. [Usage Workflow](#usage-workflow)
5. [Sample Results](#sample-results)

## Overview

The analysis focuses on bridging the gap between academic descriptions and standardized skill taxonomies (like ESCO or O*NET). It uses a refactored skill extraction engine to identify raw skills and align them with recognized professional definitions.

## Installation

To run this analysis, install the required dependencies:

```bash
pip install laiser pandas matplotlib seaborn torch
```

## Key Features

- **Automated Extraction**: Uses LLMs (for example, Gemini) to parse natural language program descriptions.
- **Skill Alignment**: Maps extracted terms to standardized taxonomies with correlation coefficients.
- **Visualization**: Generates distribution plots of skills across different academic programs.

## Usage Workflow

### 1. Initialization

Configure `SkillExtractorRefactored` with your model ID and API key.

### 2. Data Preparation

Load program data into a pandas DataFrame containing at least an ID, name, and description.

### 3. Extraction

Run `extract_and_align` to generate a structured skill report.

### 4. Visualization

Merge results with original metadata to visualize skill density per program.

## Sample Results

Based on the current implementation, the system extracts the following:

- **Computer Science**: software development, algorithms, data structures, and related skills.
- **Data Science**: machine learning, statistical modeling, R, Python, and related skills.
- **Mechanical Engineering**: thermodynamics, CAD software, robotics, and related skills.

## Credits

- Developed by Satya Phanindra Kumar Kalaga
- Updated by Udit Chowdary Jasti
