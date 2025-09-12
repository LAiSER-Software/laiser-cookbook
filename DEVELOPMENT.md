# Development Environment Setup

This guide helps contributors set up their local development environment for working with LAiSER Cookbook.

## 🚀 Quick Setup

### Prerequisites
- Python 3.7 or higher
- Git
- A Hugging Face account and API token

### 1. Clone the Repository
```bash
git clone https://github.com/LAiSER-Software/laiser-cookbook.git
cd laiser-cookbook
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Using venv
python -m venv laiser-cookbook-env
source laiser-cookbook-env/bin/activate  # On Windows: laiser-cookbook-env\Scripts\activate

# Or using conda
conda create -n laiser-cookbook python=3.9
conda activate laiser-cookbook
```

### 3. Install Jupyter
```bash
pip install jupyter notebook
# Or for JupyterLab
pip install jupyterlab
```

### 4. Set Up Hugging Face Credentials
Create a `.env` file in the project root (this file is git-ignored):
```bash
HF_TOKEN=your_hugging_face_token_here
MODEL_ID=mistralai/Mistral-7B-Instruct-v0.1
```

## 🧪 Testing Notebooks

### Running a Recipe
1. Navigate to a recipe directory:
   ```bash
   cd receipes/Job_Skill_Analysis/
   ```

2. Start Jupyter:
   ```bash
   jupyter notebook
   # Or for JupyterLab
   jupyter lab
   ```

3. Open the `.ipynb` file and run all cells

### Validation Checklist
- [ ] All cells execute without errors
- [ ] Dependencies install correctly
- [ ] Visualizations render properly
- [ ] Sample data loads successfully
- [ ] Outputs match expected results

## 🔧 Development Tools

### Recommended VS Code Extensions
- Python
- Jupyter
- GitLens
- Python Docstring Generator

### Code Formatting
We recommend using these tools for consistent code style:
```bash
pip install black isort flake8
```

Format code:
```bash
black your_notebook.ipynb
isort your_notebook.ipynb
```

## 📁 Project Structure

```
laiser-cookbook/
├── .github/                 # GitHub templates and workflows
├── receipes/               # Recipe notebooks and documentation
│   ├── Job_Skill_Analysis/
│   ├── Pay_Equity_Analysis/
│   └── University_Program_Skill_Analysis/
├── CONTRIBUTING.md         # Contribution guidelines
├── SECURITY.md            # Security policy
├── README.md              # Main documentation
└── LICENSE                # License file
```

## 🎯 Creating a New Recipe

### 1. Directory Structure
Create a new directory under `receipes/`:
```bash
mkdir receipes/Your_Recipe_Name/
cd receipes/Your_Recipe_Name/
```

### 2. Required Files
- `Your_Recipe_Name.ipynb` - The main notebook
- `Readme.md` - Recipe documentation

### 3. Notebook Template
Start with this cell structure:
```python
# Cell 1: Install dependencies
!pip install laiser pandas matplotlib seaborn

# Cell 2: Imports
import pandas as pd
import matplotlib.pyplot as plt
# ... other imports

# Cell 3: Setup credentials
from getpass import getpass
hf_token = getpass("Enter your Hugging Face token: ")
model_id = input("Enter model ID (default: mistralai/Mistral-7B-Instruct-v0.1): ") or "mistralai/Mistral-7B-Instruct-v0.1"

# ... rest of your notebook
```

### 4. README Template
Use this structure for your README.md:
```markdown
# Recipe Name

## 📜 Narrative: [Problem Description]
[Explain the real-world scenario this recipe addresses]

## 📋 What to Know Before You Start
[Prerequisites and setup information]

### 1. API Credentials Required
[Hugging Face setup instructions]

### 2. Dependencies will be Installed
[Dependency information]

### 3. No Special Hardware Needed
[Hardware requirements]

### 4. The Dataset
[Data source and customization instructions]
```

## 🚨 Common Issues

### Notebook Won't Run
- Check Python version (3.7+)
- Verify Hugging Face token is valid
- Ensure internet connection for package installation

### API Errors
- Verify Hugging Face token permissions
- Check model availability
- Consider rate limiting

### Import Errors
- Restart kernel after installing packages
- Check virtual environment activation
- Update pip: `pip install --upgrade pip`

## 🔄 Git Workflow

### Creating a Feature Branch
```bash
git checkout -b feature/recipe-name
# Make your changes
git add .
git commit -m "Add: descriptive message"
git push origin feature/recipe-name
```

### Keeping Your Fork Updated
```bash
git remote add upstream https://github.com/LAiSER-Software/laiser-cookbook.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## 📞 Getting Help

- **Issues**: Use GitHub issues for bugs and questions
- **Discussions**: Use GitHub discussions for general questions
- **Contributing**: Read `CONTRIBUTING.md` for detailed guidelines

Happy coding! 🎉