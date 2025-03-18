# Job Description Summarizer

## Overview

The **Job Description Summarizer** is a **Streamlit** application that uses **LangChain** and **Google’s Gemini-1.5-Pro model** to generate concise and structured summaries of job descriptions. It extracts key details such as **responsibilities, requirements, and suggested resume highlights** to help job seekers and recruiters quickly understand job postings.

## Features

- **AI-Powered Summarization** – Uses **Gemini-1.5-Pro** via **LangChain** for advanced text processing
- **Detailed Skill Extraction** – Identifies key **skills, responsibilities, and project types**
- **Resume Optimization Advice** – Provides insights on how to tailor resumes for each job
- **Job Market Insights** – Offers trends, in-demand skills, and career growth opportunities
- **User-Friendly Web Interface** – Built using **Streamlit** for easy interaction

## Demo

Experience the live application: [Job Description Summarizer](https://job-description-summarizer.onrender.com)

## Tech Stack

- **Python** – Backend logic
- **Streamlit** – Web-based user interface
- **LangChain** – Orchestrating LLM responses
- **Google Gemini-1.5-Pro API** – AI-based text summarization
- **dotenv** – Secure API key management

## Installation & Setup

### 1. Clone the repository:

```bash
git clone https://github.com/PriyanshuLathi/Job-Description-Summarizer.git
cd Job-Description-Summarizer
```

### 2. Create and Activate a Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up Gemini API key:

Create a `.env` file in the project root and add your Gemini API key:

```bash
API_KEY=your_api_key_here
```

### 5. Run the application:

```bash
streamlit run app.py
```

## Usage

- Open the web interface.
- Enter the Job Role, Location, Industry, and Job Description.
- Click Summarize, and the AI will extract key details.
- View additional **Job Market Insights** for trends and career guidance.

## Project Structure

```bash
📂 Job-Description-Summarizer
│── app.py                # Main app
│── requirements.txt      # Dependencies
│── .env                  # API key storage (ignored in .gitignore)
│── README.md             # Documentation
```

## Example

### Input:

```bash
Role: Data Scientist
Location: Remote
Industry: Technology
Job Description: We are looking for a Data Scientist with experience in Python, machine learning, and NLP.
```

### Output (Shortened):

```bash
- Job Title: Data Scientist
- Responsibilities: Data analysis, model development, and performance optimization
- Requirements: Python, ML, NLP, statistical modeling
- Projects: Predictive modeling, NLP-based applications
- Resume Advice: Highlight Python expertise, feature ML projects with real-world impact

📊 Job Market Insights:
- **Trends**: Increasing demand for AI-driven analytics
- **In-Demand Skills**: Python, deep learning, big data
- **Growth Potential**: High job growth in AI-related fields
- **Common Interview Questions**: Explain a machine learning model you've built.
```

## Conclusion

The **Job Description Summarizer using LangChain & Gemini** leverages AI to efficiently extract key insights from job descriptions, helping job seekers and recruiters save time while optimizing resumes for specific roles. By utilizing **Google's Gemini-1.5-Pro model** with **LangChain**, this tool provides structured and actionable insights tailored to each job posting.

With an intuitive **Streamlit** interface and secure API key management via **dotenv**, the application is easy to use and deploy. Future improvements could include **multi-language support, enhanced summarization models,** and **integration with job boards**.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-branch-name.

```bash
git checkout -b feature-branch-name
```

3. Make your changes and commit them: git commit -m 'Add new feature'.

```bash
git commit -m "Add new feature"
```

4. Push to the branch: git push origin feature-branch-name.

```bash
git push origin feature-branch-name
```

5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PriyanshuLathi/Job-Description-Summarizer/blob/main/LICENSE) file for details.

## Contact

For questions or feedback:

- LinkedIn: [Priyanshu Lathi](https://www.linkedin.com/in/priyanshu-lathi)
- GitHub: [Priyanshu Lathi](https://github.com/PriyanshuLathi)

## Authors

- Priyanshu Lathi
