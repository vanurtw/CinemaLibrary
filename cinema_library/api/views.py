from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieSerializer, CategorySerializers, GenreSerializers
from movie.models import Movie, Categories, Genre
from rest_framework import viewsets
from .filters import MovieFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .serializers_mixins import YearSerializerMixin
from rest_framework.response import Response


class MovieViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filterset_class = MovieFilter
    filter_backends = [DjangoFilterBackend]


class LastMovieAPIView(GenericAPIView, ListModelMixin):
    serializer_class = MovieSerializer
    pagination_class = None

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        queryset = Movie.objects_active.order_by('-date_create')[:4]
        return queryset


class CategoryAPIView(GenericAPIView, ListModelMixin):
    serializer_class = CategorySerializers
    pagination_class = None
    queryset = Categories.objects.all()

    def get(self, request):
        return self.list(request)


class GenreAPIView(GenericAPIView, ListModelMixin):
    serializer_class = GenreSerializers
    pagination_class = None
    queryset = Genre.objects.all()

    def get(self, request):
        return self.list(request)


class YearsAPIView(GenreAPIView, YearSerializerMixin):
    pagination_class = None
    queryset = Movie.objects.all().distinct('premiere')

    def get(self, request):
        serizlizer_data = self.get_data_serializer_mixin('premiere')
        return Response({'years': serizlizer_data})
