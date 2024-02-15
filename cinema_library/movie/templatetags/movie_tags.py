from django.template import Library
from movie.models import Genre, Movie, Categories

register = Library()


@register.simple_tag(name='genry_tags')
def genry_tags():
    genres = Genre.objects.all()
    return genres


@register.simple_tag(name='genre_movie')
def genry_movie():
    categories = Categories.objects.all()
    return categories


# @register.simple_tag(name='range_star')
# def range_star(count=5):
#     return range(count)
@register.filter(name='range_star')
def range_star(count=5):
    return range(int(count))


@register.inclusion_tag(filename='tags/year_paid_side.html', name='year_side')
def year_side_paid():
    movie = Movie.objects.values_list('premiere').distinct().order_by('premiere')
    return {'movie': movie}


@register.inclusion_tag(filename='tags/last_append.html', name='last_append')
def last_append():
    last_movie_create = Movie.objects.all().order_by('-date_create')[:4]
    return {'last_movie_create': last_movie_create}
