from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .serializers import MovieSerializer
from movie.models import Movie, Categories
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .filters import MovieFilter
from rest_framework.pagination import PageNumberPagination


class MovieViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filterset_class = MovieFilter
    filter_backends = [DjangoFilterBackend]
