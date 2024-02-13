from django.urls import path
from .views import MovieListView, MovieDetailView, ReviewHandle

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', ReviewHandle.as_view(), name='review_handle'),

]
