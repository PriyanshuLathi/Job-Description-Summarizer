import streamlit as st
from summarizer import summarize_jd

st.set_page_config(page_title="Job Description Summarizer", page_icon="📜", layout="wide")

st.title("Job Description Summarizer", anchor=False)
st.header("Summarize Job Description with AI", anchor=False)

with st.form("my_form"):
    
    role = st.text_input("Role", value="")
    location = st.text_input("Location", value="")
    industry = st.text_input("Industry", value="")
    jd = st.text_area("Paste the job description here", value="")

    submit = st.form_submit_button(label="Summarize")

if submit:
    if jd and industry and location and role:
        with st.spinner("Processing... Please wait ⏳"):
            result = summarize_jd(jd, industry, location, role)
        st.write(result)
    else:
        st.error("Please fill in all fields.")
