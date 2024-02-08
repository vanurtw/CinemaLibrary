from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from .models import Movie


# Create your views here.


class MovieListView(ListView):
    template_name = 'movie/movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    template_name = 'movie/moviesingle.html'
    model = Movie
    slug_url_kwarg = 'slug'



