import streamlit as st
import google.generativeai as genai

api_key = st.secrets["API_KEY"]

def summarize_jd(industry, location, role, job_description):
    template = f"""
    You are a career services professional with over 10 years of experience in the {industry} primarily operating in the {location}. You are tasked with finding skills from a job description for the role of {role}. Here is the job description:

    {job_description}

    Please analyze this job description to identify the skills, and categorize them as follows:

    - Job Title: Assess the job title as it may contain key terms that should be mirrored in the resume.
    - Responsibilities: Focus on responsibilities and action verbs that align with the role.
    - Requirements: Look for requirements such as skills, education, experience, and certifications.
    - Projects: Type of projects one should have on resume.

    Advise on how these identified skills can be effectively highlighted in a resume to ensure it aligns well with the requirements of this role. Please avoid cliches and generic answers, focusing on unique and specific insights related to the provided job description. Feel free to ask me as many follow-up questions as you'd like to clear any doubts, once you're done satisfying my current request.
    """
    
    if not api_key:
        raise ValueError("API key is missing. Please set the API key.")
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(template)

    return response.text
