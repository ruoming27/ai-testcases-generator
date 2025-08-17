import streamlit as st
from backend.ai_generator import generate_test_cases  # adjust import if needed

st.title("AI Test Case Generator")

requirement = st.text_input("Enter requirement:")

if st.button("Generate Test Cases"):
    if requirement:
        test_cases = generate_test_cases(requirement)
        st.subheader("Generated Test Cases")
        for i, case in enumerate(test_cases, start=1):
            st.markdown(f"**{i}. {case['description']}**")
            st.markdown(f"- Steps: {case['steps']}")
            st.markdown(f"- Expected: {case['expected_result']}")
    else:
        st.warning("Please enter a requirement!")
