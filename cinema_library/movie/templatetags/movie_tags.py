from django.template import Library
from movie.models import Genre, Movie

register = Library()


@register.simple_tag(name='genry_tags')
def genry_tags():
    genres = Genre.objects.all()
    return genres


@register.inclusion_tag(filename='tags/year_paid_side.html', name='year_side')
def year_side_paid():
    movie = Movie.objects.values('premiere').distinct()
    return {'movie': movie}
