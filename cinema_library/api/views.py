from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import HomeListSerializer
from movie.models import Movie
from rest_framework.response import Response
from rest_framework.generics import views
from rest_framework import viewsets


class ListViewAPI(APIView):
    def get(self, request):
        star = request.GET.get('star')
        queryset = Movie.objects.all()
        if star:
            queryset = queryset.filter(rating=star)
        serializer = HomeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pk = request.data.get('pk')
        if not pk:
            return Response({'error': 'not pk'})
        instance = get_object_or_404(Movie, pk=pk)
        serializer = HomeListSerializer(instance=instance, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class HomeViewListGeneric(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = HomeListSerializer

