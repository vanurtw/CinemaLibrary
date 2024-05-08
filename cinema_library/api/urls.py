from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('movie', views.MovieViewsets)

urlpatterns = [
    path('', include(router.urls)),
    # path('categories-all/', views.CategoryAPI.as_view()),
    # path('year-all/', views.YearAPI.as_view()),
    # path('movie-detail/<int:pk>/', views.MovieDetail.as_view()),
    #
    #

]
