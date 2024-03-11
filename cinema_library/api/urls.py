from django.urls import path, include
from . import views
from rest_framework import routers




urlpatterns = [
    path('movie-all/', views.ListViewAPI.as_view()),
    path('categories-all/', views.CategoryAPI.as_view()),
    path('year-all/', views.YearAPI.as_view()),



]
