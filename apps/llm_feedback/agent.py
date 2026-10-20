import json
import ollama

MODEL = "llama3.1"

PROMPT = """You are a code reviewer. Review the solution below and reply ONLY with JSON in exactly this format:

{{
  "problems": ["bug or issue 1", "bug or issue 2"],
  "suggestions": ["suggestion 1", "suggestion 2"],
  "time_complexity": "O(...)",
  "space_complexity": "O(...)",
  "related_topics": ["topic 1", "topic 2"]
}}

Use an empty list for "problems" if the code has no issues.

Problem: {title}
{content}

Language: {lang}
Code:
{code}
"""


def evaluate_code(context):
    prompt = PROMPT.format(
        title=context["title"],
        content=context["content"],
        lang=context["lang"],
        code=context["code"],
    )

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            format="json",
        )
        return json.loads(response["message"]["content"])
    except Exception as e:
        return {"error": str(e)}