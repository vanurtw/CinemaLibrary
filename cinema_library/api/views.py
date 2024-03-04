from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import HomeListSerializer
from movie.models import Movie
from rest_framework.response import Response


class ListViewAPI(APIView):
    def get(self, request):
        star = request.GET.get('star')
        queryset = Movie.objects.all()
        if star:
            queryset = queryset.filter(rating=star)
        serializer = HomeListSerializer(queryset, many=True)
        return Response(serializer.data)
