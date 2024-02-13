from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

# Create your models here.

# Категории
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


# Режиссеры/Актеры
class DirectorsActors(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    image = models.ImageField(upload_to='directors_actors', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер/Актер'
        verbose_name_plural = 'Режиссеры/Актеры'


# Жанраы
class Genre(models.Model):
    title = models.CharField(verbose_name='Жанр', max_length=255)
    slug = models.SlugField(verbose_name='Слаг', max_length=255)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


# Фильмы
class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField()
    tagline = models.CharField(max_length=255, verbose_name='Слоган', blank=True)
    content = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='poster/', verbose_name='Постер', blank=True)
    data_movie = models.DateTimeField(verbose_name='Дата выхода фильма')
    country = models.CharField(max_length=255, verbose_name='Страна')
    director = models.ManyToManyField(DirectorsActors, verbose_name='Режисер', related_name='director_movies')
    actors = models.ManyToManyField(DirectorsActors, verbose_name='Актеры', related_name='actor_movies')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    premiere = models.CharField(
        max_length=255,
        verbose_name='Премьера в мире',
    )
    budget = models.CharField(max_length=255, verbose_name='Бюджет')
    url = models.URLField(blank=True, verbose_name='Ссылка на трейлер фильма')
    fees_world = models.CharField(max_length=255, verbose_name='Cборы в мире')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    active = models.BooleanField(default=True, verbose_name='Активный')
    date_create = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


# Кадры из фильмов
class StillsFilm(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='stills_film', verbose_name='зображения из фильма')
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм', related_name='stills_films')

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильмов'


# Звезды рейтинга
class RatingStars(models.Model):
    rating = models.PositiveIntegerField(verbose_name='Значение рейтинга')

    class Meta:
        verbose_name = 'Значения рейтинга'
        verbose_name_plural = 'Значение рейтинга'


# Рейтинг
class Rating(models.Model):
    rating = models.ForeignKey(RatingStars, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


# Отзывы
class Reviews(models.Model):
    # user = models.ForeignKey(get_user_model())
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(verbose_name='Комментарий')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Родитель')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'
