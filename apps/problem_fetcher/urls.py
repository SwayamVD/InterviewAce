from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='problem'),
    path("category/<str:slug>/", views.category_list, name="category_list"),
    path("search/<str:keyword>/", views.search_list, name="search_list_path"),
    path("search/", views.search_list, name="search_list"),
    path("problem/<str:title_slug>/", views.problem_detail, name="problem_detail"),
]