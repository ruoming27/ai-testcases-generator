from fastapi import FastAPI
from pydantic import BaseModel
from .db import init_db, fetch_test_cases, save_test_case
from .ai_generator import generate_test_cases, parse_ai_output

app = FastAPI()

# Initialize DB
init_db()


@app.get("/")
def home():
    return {"message": "AI Test Case Generator is running!"}


class Requirement(BaseModel):
    requirement: str


@app.post("/generate/")
def generate(req: Requirement):
    # 1. Call AI
    raw_output = generate_test_cases(req.requirement)
    # 2. Parse JSON safely
    test_cases = parse_ai_output(raw_output)
    # 3. Save to DB
    for case in test_cases:
        save_test_case(case["description"], case["steps"],
                       case["expected_result"])
    return test_cases


@app.get("/test_cases/")
def get_test_cases():
    return fetch_test_cases()
