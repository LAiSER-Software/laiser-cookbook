# README: University Program Skill Analysis

## 📜 Narrative: What Skills Are We Teaching?

A university's leadership team—deans, department heads, and curriculum designers—faces a constant challenge: ensuring that their programs are relevant and aligned with industry demands. How can they get a quick, consistent, and high-level overview of the skills taught across dozens or even hundreds of different programs? Reading through every syllabus or program description manually is impractical and subjective.

This notebook provides a solution for that team. It uses AI to read through program descriptions and extract a standardized list of skills. By visualizing this data, administrators can easily compare programs, identify overlaps, spot potential curriculum gaps, and ensure that what they *say* they are teaching aligns with the actual skills students are gaining. This data-driven approach is invaluable for strategic planning, program marketing, and accreditation reporting.

## 📋 What to Know Before You Start

Here are a few key points to understand before running this notebook.

### 1. **API Credentials Required**
The `laiser` package uses AI models from the Hugging Face Hub. To access these models, you will need to provide your credentials.

* **Hugging Face Account**: You'll need a free account on [Hugging Face](https://huggingface.co/join).
* **Hugging Face Token**: Generate a User Access Token with `read` permissions from your account settings.
* **Model ID**: Choose a model for the extraction, for example, `"mistralai/Mistral-7B-Instruct-v0.1"`.

You will be asked to enter your `model_id` and `hf_token` in **Cell 7** of the notebook.

### 2. **Dependencies will be Installed**
The notebook will automatically install all required Python libraries, including `laiser`, `pandas`, `matplotlib`, and `seaborn`, using a `!pip install` command in the first code cell. No manual installation is needed.

### 3. **No Special Hardware Needed**
This notebook is configured to run on a standard CPU. A GPU is not required, so you can run it on a personal laptop or a free cloud-based notebook service.

### 4. **The Dataset is a Sample**
For demonstration purposes, this notebook uses a small, manually created DataFrame to represent university program data. You can easily modify **Cell 9** to load your own data from a CSV file or another source. The `input_type` for the extractor is set to `'syllabus'`, which is suitable for academic texts like program descriptions.
