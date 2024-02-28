from django.test import TestCase
from .models import Movie
# Create your tests here.


class MovieTest(TestCase):
    def test_home_movie(self):
        movies = Movie.objects.all()
        self.assertQuerySetEqual(movies, )