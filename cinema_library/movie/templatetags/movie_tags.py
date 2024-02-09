from django.template import Library
from movie.models import Genre, Movie

register = Library()


@register.simple_tag(name='genry_tags')
def genry_tags():
    genres = Genre.objects.all()
    return genres


@register.inclusion_tag(filename='tags/year_paid_side.html', name='year_side')
def year_side_paid():
    movie = Movie.objects.values_list('premiere').distinct().order_by('premiere')
    return {'movie': movie}


@register.inclusion_tag(filename='tags/last_append.html', name='last_append')
def last_append():
    last_movie_create = Movie.objects.all().order_by('-date_create')[:4]
    return {'last_movie_create': last_movie_create}
