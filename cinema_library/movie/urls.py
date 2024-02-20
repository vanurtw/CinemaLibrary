from django.urls import path
from .views import MovieListView, MovieDetailView, ReviewHandle, MovieFilterView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(MovieListView.as_view()), name='home'),
    path('movie-filtering/', cache_page(60)(MovieFilterView.as_view()), name='movie_filtering'),
    path('<slug:slug>/', cache_page(5)(MovieDetailView.as_view()), name='movie_detail'),
    path('review/<int:pk>/', ReviewHandle.as_view(), name='review_handle'),
]
