import streamlit as st
import requests

st.set_page_config(page_title="AI Job Interview Coach", layout="centered")

st.title("🎯 AI Job Interview Coach")
st.write("Get interview practice with AI-generated questions, answers, and feedback.")

role = st.text_input("Enter the job role (e.g. Software Engineer, Data Scientist):")

if st.button("Start Interview"):
    if role.strip() == "":
        st.warning("Please enter a job role.")
    else:
        with st.spinner("Interview in progress..."):
            response = requests.post("http://127.0.0.1:8000/interview", json={"role": role})
            if response.status_code == 200:
                data = response.json()

                st.subheader("📝 Interview Questions")
                st.write(data["questions"])

                st.subheader("💡 Candidate Answers")
                st.write(data["answers"])

                st.subheader("📊 Feedback")
                st.write(data["feedback"])

                st.success("✅ Interview simulation completed!")
            else:
                st.error("Something went wrong with the backend request.")
