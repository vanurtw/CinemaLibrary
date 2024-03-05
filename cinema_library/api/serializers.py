from rest_framework import serializers


class HomeListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    tagline = serializers.CharField(max_length=255)
    rating = serializers.IntegerField()
    images = serializers.CharField(source='poster')
