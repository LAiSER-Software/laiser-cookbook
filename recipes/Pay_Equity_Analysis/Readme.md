# Pay Equity Analysis Based on Skills

- Author: Satya Phanindra Kumar Kalaga
- Date: September 2025

## 📜 Narrative: Are We Paying for Skills or Just Titles?

An HR analytics team is tasked with a critical mission: ensuring fair and equitable compensation across the company. Traditionally, salaries are tied to job titles, but this can lead to inconsistencies. A "Data Analyst" at one level might possess a more complex and in-demand skill set than a "Manager" in a different department, yet their compensation might not reflect that. How can the team move beyond titles to ensure people are paid fairly for the skills they bring to the table?

This notebook is their tool for investigation. It allows the team to extract the specific skills required for each role directly from job descriptions and map them against salary data. By visualizing the relationship between the *number* of required skills and compensation, they can spot anomalies at a glance. This data-driven approach helps identify potential pay equity issues, justify compensation strategies, and build a more transparent and fair pay structure for the entire organization.

## 📋 What to Know Before You Start

Here are the essential points to understand before running this notebook.

### 1. **API Credentials Required**
The skill extraction process is powered by the `laiser` package, which uses AI models from the Hugging Face Hub. You will need your own credentials to use it.

* **Hugging Face Account**: You will need a free account on [Hugging Face](https://huggingface.co/join).
* **Hugging Face Token**: You must generate a User Access Token with `read` permissions from your account settings.
* **Model ID**: You need to specify a model for the extraction (e.g., `"mistralai/Mistral-7B-Instruct-v0.1"`).

These credentials must be entered in the designated cell within the notebook.

### 2. **Dependencies will be Installed**
The notebook is self-contained and will install all the necessary Python libraries for you. The first code cell includes a `!pip install` command to download and set up `laiser`, `pandas`, `matplotlib`, and `seaborn`.

### 3. **No Special Hardware Needed**
This notebook is configured to run on a standard CPU. You do not need access to a GPU, making it easy to run on a personal computer or a standard cloud notebook environment.

### 4. **Sample Data is Used**
To make the notebook easy to run, it includes a small, sample dataset created directly in the code. This data represents a few job roles with descriptions and salaries. You can adapt the code in **Cell 9** to load your company's actual job and compensation data from a CSV file or other data source for a real-world analysis.
