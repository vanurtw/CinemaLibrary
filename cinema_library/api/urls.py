from django.urls import path
from . import views

urlpatterns = [
    path('movie-all/', views.ListViewAPI.as_view()),

]
