from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Movie, Reviews, Categories, RatingStars, Genre
from .forms import ReviewsForm
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.


class MovieListView(ListView):
    template_name = 'movie/movies.html'
    context_object_name = 'movies'

    def get_queryset(self, *args, **kwargs):
        category = self.request.GET.get('category', None)
        if category:
            return Movie.objects.filter(category__slug=category)
        return Movie.objects.all()

    def post(self, request, **kwargs):
        search_post = request.POST.get('search')
        movies = Movie.objects.filter(title__icontains=search_post)
        return render(request, 'movie/movies.html', {'movies': movies})

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        ratings_star = RatingStars.objects.all()
        context['ratings_star'] = ratings_star
        return context


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
            parent_id = request.POST.get('parent', None)
            form = form.save(commit=False)
            form.movie = movie
            if parent_id:
                parent_comment = Reviews.objects.get(id=parent_id)
                form.parent = parent_comment
            form.save()
        return redirect(movie.get_absolute_url())

    def get(self, request, **kwargs):
        movie_id = kwargs.get('pk')
        movie = get_object_or_404(Movie, id=movie_id)
        parent_id_comment = request.GET.get('parent')
        parent_comment = Reviews.objects.get(id=parent_id_comment)
        form = ReviewsForm()
        form.initial['text'] = f'{parent_comment.name}, '
        return render(request, 'movie/moviesingle.html',
                      {'parent_comment': parent_id_comment, 'movie': movie, 'form': form, })


class MovieFilterView(View):
    def get(self, request):
        star = request.GET.get('star', None)
        if star:
            movies = Movie.objects.filter(rating__rating=star)
            ratings_star = RatingStars.objects.all()
            return render(request, 'movie/movies.html', {'movies': movies, 'ratings_star': ratings_star})
        genres = request.GET.getlist('genre')
        if genres:
            movies = Movie.objects.filter(genre__title__in=genres).distinct()
        years = request.GET.getlist('year')
        if years:
            if genres:
                movies = movies.filter(premiere__in=years)
            else:
                movies = Movie.objects.filter(premiere__in=years)
        if not (genres or years):
            messages.error(request, 'Филтры не были выбраны')
            movies = Movie.objects.all()
        return render(request, 'movie/movies.html', {'movies': movies})
