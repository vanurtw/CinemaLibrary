from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Movie
from .forms import ReviewsForm


# Create your views here.


class MovieListView(ListView):
    template_name = 'movie/movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    template_name = 'movie/moviesingle.html'
    model = Movie
    slug_url_kwarg = 'slug'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ReviewsForm()
        context['form'] = form
        return context


class ReviewHandle(View):
    def post(self, request, **kwargs):
        movie_id = kwargs.get('pk')
        movie = get_object_or_404(Movie, id=movie_id)
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
