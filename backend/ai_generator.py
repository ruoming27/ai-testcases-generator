import os
import re
import json
from openai import OpenAI
from .db import save_test_case

# Load OpenAI key from env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_test_cases(requirement_text: str):
    """
    Calls OpenAI to generate test cases based on the requirement_text.
    Returns raw AI output.
    """
    prompt = f"""
    Generate a JSON array of test cases ONLY. Each object must have:
    description (string), steps (array of strings), expected_result (string)
    Do NOT include any extra text or markdown.
    Requirement: "{requirement_text}"
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw_output = response.choices[0].message.content
        print("AI raw output:", raw_output)  # DEBUG
        return raw_output

    except Exception as e:
        print(f"❌ AI generator error: {e}")
        # Return placeholder if API call fails
        return '[{"description": "Placeholder test case", "steps": ["Step 1"], "expected_result": "Expected outcome"}]'


def parse_ai_output(raw_output: str):
    """
    Extracts JSON array from raw AI output.
    Returns a list of test case dicts.
    """
    match = re.search(r'(\[.*\])', raw_output, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}")
    # Return a placeholder test case if parsing fails
    return [{"description": "Placeholder test case", "steps": ["Step 1"], "expected_result": "Expected outcome"}]
