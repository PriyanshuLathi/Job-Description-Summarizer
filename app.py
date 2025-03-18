import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# Environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    st.error("API key is missing. Please set the API key in the .env file.")
    st.stop()

# Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=api_key)

# Prompt template
prompt_template = PromptTemplate(
    input_variables=["industry", "location", "role", "job_description"],
    template="""
    You are an expert in the {industry} field, operating in {location}. Your task is to extract key information from the given job description for the role of {role}.
    
    Job Description:
    {job_description}
    
    Identify and categorize the following:
    - **Job Title**: Extract the main job title.
    - **Responsibilities**: Highlight key responsibilities.
    - **Requirements**: List essential skills, qualifications, and experience.
    - **Projects**: Suggest types of projects a candidate should highlight.
    - **Salary Range**: Identify any mentioned salary information.
    - **Benefits & Perks**: Summarize provided benefits such as healthcare, bonuses, work-from-home options, etc.
    - **Company Culture**: Identify any values, work environment details, or cultural elements mentioned.
    - **Career Growth Opportunities**: Highlight any training programs, career advancement paths, or mentorship initiatives.

    Additionally, provide insights on how a candidate can tailor their resume based on this job description.
    """
)

# Job market insights prompt template
insights_prompt_template = PromptTemplate(
    input_variables=["industry", "role"],
    template="""
    **Job Market Insights**
    Based on the {role} role in the {industry} industry, provide insights into:
    - **Current Job Market Trends**
    - **In-Demand Skills**
    - **Growth Potential in the Next 5 Years**
    - **Common Interview Questions for This Role**
    """
)

def summarize_jd(industry, location, role, job_description):
    # LLM chain
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({
        "industry": industry,
        "location": location,
        "role": role,
        "job_description": job_description
    })
    return response

def get_job_insights(industry, role):
    chain = LLMChain(llm=llm, prompt=insights_prompt_template)
    response = chain.run({"industry": industry, "role": role})
    return response

# Streamlit UI
st.set_page_config(page_title="Job Description Summarizer", page_icon="📜", layout="wide")
st.title("Job Description Summarizer")
st.header("Summarize Job Description with AI")

with st.form("my_form"):
    role = st.text_input("Role", value="")
    location = st.text_input("Location", value="")
    industry = st.text_input("Industry", value="")
    jd = st.text_area("Paste the job description here", value="")
    submit = st.form_submit_button(label="Summarize")

if submit:
    if jd and industry and location and role:
        with st.spinner("Processing... Please wait ⏳"):
            result = summarize_jd(industry, location, role, jd)
            insights = get_job_insights(industry, role)
        
        with st.expander("📄 Job Summary", expanded=True):
            st.write(result)
        
        with st.expander("📊 Job Market Insights", expanded=True):
            st.write(insights)
    else:
        st.error("Please fill in all fields.")

