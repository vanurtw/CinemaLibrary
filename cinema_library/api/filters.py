import django_filters
from movie.models import Movie, Genre


class MovieFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='slug__icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='slug__icontains')

    class Meta:
        model = Movie
        fields = ['rating', 'genre', 'title', 'category', 'premiere']
