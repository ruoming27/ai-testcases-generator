🧪 AI Test Case Generator

An AI-powered tool to automatically generate software test cases from requirements. Built with FastAPI, Streamlit, and OpenAI.

Features

Generate test cases from natural language requirements using OpenAI.

Store generated test cases in a PostgreSQL database.

Interactive web interface via Streamlit.

Works both locally and on Streamlit Cloud.

Tech Stack

Python 3.11+

FastAPI (backend API)

Streamlit (frontend UI)

OpenAI API (AI test case generation)

PostgreSQL (database)

python-dotenv (for local environment variables)

Getting Started (Local Development)
1. Clone the repository
git clone https://github.com/ruoming27/ai-testcases-generator.git
cd ai-testcases-generator

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Windows (PowerShell)

.\venv\Scripts\Activate


macOS/Linux

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure environment variables

Create a .env file in the project root:

OPENAI_API_KEY=sk-xxxx
POSTGRES_DB=testcase_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass4SQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432


Note: .env should not be uploaded to GitHub.

6. Run locally
streamlit run app.py


Open your browser at: http://localhost:8501

Enter a requirement and generate test cases.

Deployment on Streamlit Cloud

Push your repository to GitHub.

Go to Streamlit Cloud and connect your GitHub repo.

Set Secrets for environment variables (OPENAI_API_KEY, PostgreSQL credentials).

Deploy your app.

Set Sharing → Public to make it accessible to anyone.

Project Structure
ai-testcases-generator/
│
├─ backend/
│  ├─ __init__.py
│  ├─ ai_generator.py      # AI test case generation logic
│  ├─ db.py                # PostgreSQL database functions
│
├─ app.py                  # Streamlit frontend
├─ requirements.txt
├─ .env                    # Local environment variables (ignored by git)
├─ README.md

Usage

Enter a software requirement in the input box.

Click Generate Test Cases.

View generated test cases with description, steps, and expected results.

Notes

Local development: requires .env file.

Streamlit Cloud deployment: use Secrets for environment variables.

PostgreSQL must be running locally for local testing.

License

This project is open-source under the MIT License.

✅ How to upload this to GitHub

Save this as README.md in your project root.

Stage and commit the file:

git add README.md
git commit -m "Add public README"


Push to GitHub:

git push origin main
