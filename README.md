# InterviewAce

A Django-based interview preparation platform that helps users practice coding problems, run code, and receive AI-powered feedback.

## Features

- **Problem Fetcher**: Retrieve and manage coding interview problems
- **Code Runner**: Execute and test code submissions
- **LLM Feedback**: Get AI-powered feedback on your solutions

## Setup

1. Clone the repository and create a virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:

   ```bash
   cp .env.example .env
   ```

4. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Environment Variables

See `.env` for configuration options (LOCAL_LLM_URL, LEETCODE_API_URL, etc.)
