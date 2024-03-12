from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import HomeListSerializer, CategorySerializer, YearSerializer, MovieSerializerDetail
from movie.models import Movie, Categories
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins


class ListViewAPI(APIView):
    def get(self, request):
        queryset = Movie.objects.all()
        serializer = HomeListSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryAPI(APIView):
    def get(self, request):
        queryset = Categories.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class YearAPI(APIView):
    def get(self, request):
        queryset = Movie.objects.all().distinct()
        serializer = YearSerializer(queryset, many=True)
        return Response(serializer.data)


class MovieDetail(APIView):
    def get(self, request, pk):

        queryset = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializerDetail(queryset)

        return Response(serializer.data)





