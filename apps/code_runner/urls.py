from django.urls import path
from django.http import JsonResponse
from . import views
urlpatterns = [
    path("", views.editor, name='runner'),
    path("solve/", views.solve_problem, name="solve_problem"),
    path("evaluate/", views.evaluate_problem, name="evaluate"),
    path("execute/", views.execute_code, name="execute_code"),

]




# REF
# urlpatterns = [
#     path("category/<str:slug>/", views.category_list, name="category_list"),
#     path("search/<str:keyword>/", views.search_list, name="search_list_path"),
#     path("search/", views.search_list, name="search_list"),
#     path("problem/<str:title_slug>/", views.problem_detail, name="problem_detail"),
# ]