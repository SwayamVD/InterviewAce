from django.shortcuts import render
import requests


def home(request):
    data = {
        'name': 'John',
        'age': 22,
        'city': 'Nashik'
    }
    return render(request, 'home.html', data)


def about(request):
    """About page view"""
    return render(request, "problems/about.html")

