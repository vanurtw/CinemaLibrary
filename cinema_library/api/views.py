from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import HomeListSerializer, CategorySerializer
from movie.models import Movie, Categories
from rest_framework.response import Response


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
