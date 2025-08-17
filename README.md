# 🧪 AI Test Case Generator

An AI-powered tool to automatically generate software test cases from requirements. Built with FastAPI, Streamlit, and OpenAI.

## Live Demo

Check out the live web app here:
https://ai-testcases-generator-aw.streamlit.app/

## Features

- Generate test cases from natural language requirements using OpenAI.

- Store generated test cases in a PostgreSQL database.

- Interactive web interface via Streamlit.

- Works both locally and on Streamlit Cloud.

## Tech Stack

- Python 3.11+

- FastAPI (backend API)

- Streamlit (frontend UI)

- OpenAI API (AI test case generation)

- PostgreSQL (database)

- python-dotenv (for local environment variables)

## Getting Started (Local Development)
1. Clone the repository
```bash
git clone https://github.com/ruoming27/ai-testcases-generator.git

cd ai-testcases-generator
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment

Windows (PowerShell)
```bash
.\venv\Scripts\Activate
```

macOS/Linux
```bash
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Configure environment variables

Create a .env file in the project root:
```ini
OPENAI_API_KEY=sk-xxxx
POSTGRES_DB=testcase_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass4SQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Note: .env should not be uploaded to GitHub.

6. Run locally
```bash
streamlit run app.py
```
- Open your browser at: http://localhost:8501

- Enter a requirement and generate test cases.

## Deployment on Streamlit Cloud

1. Push your repository to GitHub.

2. Go to Streamlit Cloud and connect your GitHub repo.

3. Set Secrets for environment variables (OPENAI_API_KEY, PostgreSQL credentials).

4. Deploy your app.

5. Set Sharing → Public to make it accessible to anyone.

## Project Structure
```bash
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
```
## Usage

1. Enter a software requirement in the input box.

2. Click Generate Test Cases.

3. View generated test cases with description, steps, and expected results.

## Notes

- Local development: requires .env file.

- Streamlit Cloud deployment: use Secrets for environment variables.

- PostgreSQL must be running locally for local testing.

## License

This project is open-source under the MIT License.

✅ How to upload this to GitHub

1. Save this as README.md in your project root.

2. Stage and commit the file:
```bash
git add README.md
git commit -m "Add public README"
```

3. Push to GitHub:
```bash
git push origin main
```