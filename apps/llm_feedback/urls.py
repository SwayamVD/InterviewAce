from django.urls import path
from django.http import JsonResponse

urlpatterns = [
    path('', lambda r: JsonResponse({"message": "Code Runner API works!"})),
]
