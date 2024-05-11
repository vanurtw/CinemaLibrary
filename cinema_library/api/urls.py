from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('movie', views.MovieViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('last-movie/', views.LastMovieAPIView.as_view()),
    path('category/', views.CategoryAPIView.as_view()),
    path('genre/', views.GenreAPIView.as_view()),
    path('years/', views.YearsAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewsAPIView.as_view()),

]
