from backend.ai_generator import generate_test_cases, parse_ai_output
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


st.title("AI Test Case Generator")

# User input
requirement = st.text_area("Enter requirement:", "")

if st.button("Generate Test Cases") and requirement.strip():
    # Generate raw test cases from AI
    raw_output = generate_test_cases(requirement)

    # Parse AI output
    test_cases = parse_ai_output(raw_output)

    if not test_cases:
        st.warning("No test cases were generated.")
    else:
        st.success(f"{len(test_cases)} test case(s) generated!")

        # Display test cases safely
        for i, case in enumerate(test_cases, 1):
            if isinstance(case, dict):
                desc = case.get("description", "No description")
                steps = case.get("steps", "")
                expected = case.get("expected_result", "")
                st.markdown(f"**{i}. {desc}**")
                if steps:
                    st.markdown(f"- Steps: {steps}")
                if expected:
                    st.markdown(f"- Expected Result: {expected}")
            else:
                # fallback if case is just a string
                st.markdown(f"**{i}. {case}**")
