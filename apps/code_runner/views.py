from django.shortcuts import render
import json
import ast
from apps.llm_feedback.agent import evaluate_code
import docker
import tempfile
import os
from django.http import JsonResponse
# Create your views here.
def editor(request):
    return render(request, "editor/editor_page.html")


ALLOWED_LANGS = {"cpp", "python3", "java", "javascript"}

def solve_problem(request):
    context = {}
    if request.method == "POST":
        title_slug = request.POST.get("title_slug")
        title = request.POST.get("title")
        raw_snippets = request.POST.get("code_snippets")
        content = request.POST.get("content")

        # Parse the string into a list of dicts
        try:
            snippets = json.loads(raw_snippets)
        except (json.JSONDecodeError, TypeError):
            try:
                snippets = ast.literal_eval(raw_snippets)
            except (ValueError, SyntaxError):
                snippets = []

        filtered_snippets = [s for s in snippets if s["langSlug"] in ALLOWED_LANGS]
        print(filtered_snippets)

        context = {
            "title_slug": title_slug,
            "title": title,
            "code_snippets": filtered_snippets,
            "content": content,
        }
    return render(request, "editor/editor_page.html", context)

def evaluate_problem(request):
    context = {}
    print("request reached")
    if request.method == "POST":
        try:
            # Try parsing JSON from request body first
            data = json.loads(request.body)
            title = data.get("title")
            content = data.get("content")
            lang = data.get("lang")
            code = data.get("code")
        except (json.JSONDecodeError, UnicodeDecodeError):
            # Fall back to form data if JSON parsing fails
            title = request.POST.get("title")
            content = request.POST.get("content")
            lang = request.POST.get("lang")
            code = request.POST.get("code")
        
        context = {
            "title": title,
            "content": content,
            "lang": lang,
            "code": code,
        }
        agentResponse = evaluate_code(context)
        return render(request, "evaluation/evaluate_page.html", agentResponse)
    return render(request, "evaluation/evaluate_page.html", context)

def execute_code(request):
    try:
        # Parse JSON from request body
        data = json.loads(request.body)
        code = data.get("code", "")
        language = data.get("lang", "python3")
    except (json.JSONDecodeError, UnicodeDecodeError):
        # Fall back to POST if JSON fails
        code = request.POST.get("code", "")
        language = request.POST.get("lang", "python3")
    
    if not code.strip():
        return JsonResponse({"output": "", "error": "No code provided"}, status=400)
    
    images = {
        "python3": ("python:3.12-slim", "main.py", ["python", "main.py"]),
        "javascript": ("node:22-slim", "main.js", ["node", "main.js"]),
        "cpp": ("gcc:14", "main.cpp",
                ["sh", "-c", "g++ main.cpp -o main && ./main"]),
        "java": ("openjdk:21-slim", "Main.java", 
                ["sh", "-c", "javac Main.java && java Main"]),
    }

    if language not in images:
        return JsonResponse({"output": "", "error": f"Unsupported language: {language}"}, status=400)

    image, filename, command = images[language]

    try:
        with tempfile.TemporaryDirectory() as folder:
            filepath = os.path.join(folder, filename)
            with open(filepath, "w") as f:
                f.write(code)

            client = docker.from_env()

            output = client.containers.run(
                image,
                command,
                volumes={folder: {"bind": "/code", "mode": "rw"}},
                working_dir="/code",
                remove=True
            )
        
        # Decode bytes to string
        output_str = output.decode('utf-8') if isinstance(output, bytes) else str(output)
        return JsonResponse({"output": output_str, "error": None})
    
    except docker.errors.ContainerError as e:
        # Handle runtime errors in code
        error_output = e.stderr.decode('utf-8') if e.stderr else str(e)
        return JsonResponse({"output": "", "error": error_output}, status=400)
    except docker.errors.ImageNotFound:
        return JsonResponse({"output": "", "error": f"Docker image not found: {image}"}, status=500)
    except docker.errors.APIError as e:
        return JsonResponse({"output": "", "error": f"Docker error: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"output": "", "error": f"Execution error: {str(e)}"}, status=500)