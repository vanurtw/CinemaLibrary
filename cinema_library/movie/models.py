from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class DirectorsActors(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # image =


class Genre(models.Model):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name='')
    tagline = models.CharField(max_length=255, verbose_name='Слоган')
    content = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='poster/', verbose_name='Постер')
    data_movie = models.DateTimeField(verbose_name='Дата выхода фильма')
    country = models.CharField(max_length=255, verbose_name='Страна')
    director = models.ManyToManyField(DirectorsActors, verbose_name='Режисер')
    actors = models.ManyToManyField(DirectorsActors, verbose_name='Актеры')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    premiere = models.CharField(
        max_length=255,
        verbose_name='Премьера в мире',
    )
    budget = models.CharField(max_length=255, verbose_name='Бюджет')

    fees_world = models.CharField(max_length=255, verbose_name='Cборы в мире')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    active = models.BooleanField(default=True)


class StillsFilm(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='stills_film', verbose_name='зображения из фильма')
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
