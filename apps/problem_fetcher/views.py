from django.shortcuts import render
import requests

# ====================== COMMON CONFIG ======================
LC_URL = "https://leetcode.com/graphql/"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def home(request):
    return render(request,"problems/problem_home.html")

# ====================== 1. CATEGORY LIST ======================
def category_list(request, slug="array"):
    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: ""
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            total: totalNum
            questions: data {
                questionId
                questionFrontendId
                title
                titleSlug
                difficulty
                acRate
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "limit": 30,
            "skip": 0,
            "filters": {
                "tags": [slug]
            }
        }
    }

    response = requests.post(LC_URL, json=payload, headers=HEADERS)
    data = response.json()

    result = data.get("data", {}).get("problemsetQuestionList", {})
    problems = result.get("questions", [])
    total = result.get("total", 0)

    context = {
        "slug": slug,
        "category_name": slug.replace("-", " ").title(),
        "problems": problems,
        "total": total,
    }
    return render(request, "problems/problem_list.html", context)


# ====================== 2. SEARCH LIST ======================
def search_list(request, keyword=None):
    # Get keyword from path parameter or query string
    if keyword is None:
        keyword = request.GET.get("q", "").strip()

    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: ""
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            total: totalNum
            questions: data {
                questionId
                questionFrontendId
                title
                titleSlug
                difficulty
                acRate
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "limit": 30,
            "skip": 0,
            "filters": {
                "searchKeywords": keyword
            }
        }
    }

    response = requests.post(LC_URL, json=payload, headers=HEADERS)
    data = response.json()

    result = data.get("data", {}).get("problemsetQuestionList", {})
    problems = result.get("questions", [])
    total = result.get("total", 0)

    context = {
        "keyword": keyword,
        "problems": problems,
        "total": total,
    }
    return render(request, "problems/problem_list.html", context)


# ====================== 3. PROBLEM DETAIL ======================
def problem_detail(request, title_slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
            likes
            dislikes
            acRate
            topicTags {
                name
                slug
            }
            sampleTestCase
            exampleTestcases
            hints
            similarQuestions
            codeSnippets {
                lang
                langSlug
                code
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "titleSlug": title_slug
        }
    }

    response = requests.post(LC_URL, json=payload, headers=HEADERS)
    data = response.json()

    problem = data.get("data", {}).get("question")

    if not problem:
        return render(request, "problems/problem_detail.html", {
            "error": "Problem not found"
        })

    context = {
        "problem": problem
    }
    return render(request, "problems/problem_detail.html", context)