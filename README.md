# 🍳 LAiSER Cookbook

A collection of interactive Jupyter notebooks showcasing practical applications of the [LAiSER](https://github.com/LAiSER-Software/extract-module) package for AI-powered skill analysis and extraction.

## 📖 About

The LAiSER Cookbook provides ready-to-run notebooks that demonstrate real-world applications of AI-driven skill analysis across different domains. Each "recipe" is a complete, self-contained notebook that solves a specific problem using the LAiSER package.

## 🚀 Quick Start

1. **Prerequisites**: You'll need a [Hugging Face account](https://huggingface.co/join) and a User Access Token with `read` permissions
2. **Choose a Recipe**: Browse the recipes below and select one that matches your use case
3. **Run the Notebook**: Open the Jupyter notebook and follow the step-by-step instructions
4. **Customize**: Adapt the code to work with your own data

All notebooks are designed to run on standard CPU hardware and will automatically install required dependencies.

## 📚 Available Recipes

### 🔍 [Job Skill Analysis for Job Seekers](./receipes/Job_Skill_Analysis/)
**Perfect for:** Job seekers, career counselors, recruitment consultants

Extract and visualize the most in-demand skills from job postings to help job seekers focus their learning and tailor their resumes effectively.

**Key Features:**
- Automatic skill extraction from job descriptions
- Frequency analysis and visualization
- Word cloud generation for easy interpretation
- Uses sample job posting dataset (easily adaptable to your own data)

### 💰 [Pay Equity Analysis Based on Skills](./receipes/Pay_Equity_Analysis/)
**Perfect for:** HR teams, compensation analysts, organizational leaders

Analyze the relationship between required skills and compensation to identify potential pay equity issues and build fairer compensation structures.

**Key Features:**
- Skill-based compensation analysis
- Visual correlation between skill complexity and salary
- Identifies potential pay inequities beyond job titles
- Sample HR dataset included for demonstration

### 🎓 [University Program Skill Analysis](./receipes/University_Program_Skill_Analysis/)
**Perfect for:** Academic administrators, curriculum designers, program evaluators

Extract and compare skills taught across different university programs to ensure curriculum alignment with industry demands.

**Key Features:**
- Automated skill extraction from program descriptions
- Cross-program skill comparison and visualization
- Gap analysis capabilities
- Optimized for academic text processing

## 📈 Recent Updates (Latest Changes)

- **README Standardization**: Updated all recipe README files to use consistent formatting (removed "README:" prefix from titles)
- **Enhanced Documentation**: Improved narrative descriptions and setup instructions for all recipes
- **Better Organization**: Streamlined file structure and naming conventions

## 🛠️ Requirements

- Python 3.7+
- Jupyter Notebook environment (local installation or cloud service like Google Colab)
- Hugging Face account and API token
- Internet connection for package installation and model access

## 💡 Usage Tips

- **Start Simple**: Begin with the sample datasets provided in each notebook
- **API Limits**: Be mindful of Hugging Face API rate limits when processing large datasets
- **Customization**: Each notebook includes clear guidance on how to adapt the code for your specific data
- **Model Selection**: Different Hugging Face models may produce varying results - experiment to find what works best for your use case

## 🤝 Contributing

We welcome contributions! Whether it's new recipes, improvements to existing ones, or bug fixes, your input helps make this resource better for everyone.

## 📄 License

This project is licensed under the terms specified in the [LICENSE](./LICENSE) file.

## 🔗 Related Projects

- [LAiSER Package](https://pypi.org/project/laiser/) - The core Python package powering these recipes
