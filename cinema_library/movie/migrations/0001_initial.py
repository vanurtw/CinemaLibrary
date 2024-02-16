# Generated by Django 5.0.1 on 2024-02-14 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('data_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='DirectorsActors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('image', models.ImageField(blank=True, upload_to='directors_actors', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Режиссер/Актер',
                'verbose_name_plural': 'Режиссеры/Актеры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слаг')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='RatingStars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(verbose_name='Значение рейтинга')),
            ],
            options={
                'verbose_name': 'Значения рейтинга',
                'verbose_name_plural': 'Значение рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('tagline', models.CharField(blank=True, max_length=255, verbose_name='Слоган')),
                ('content', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(blank=True, upload_to='poster/', verbose_name='Постер')),
                ('data_movie', models.DateTimeField(verbose_name='Дата выхода фильма')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('premiere', models.CharField(max_length=255, verbose_name='Премьера в мире')),
                ('budget', models.CharField(max_length=255, verbose_name='Бюджет')),
                ('url', models.URLField(verbose_name='Ссылка на трейлер фильма')),
                ('fees_world', models.CharField(max_length=255, verbose_name='Cборы в мире')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('actors', models.ManyToManyField(related_name='actor_movies', to='movie.directorsactors', verbose_name='Актеры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.categories', verbose_name='Категория')),
                ('director', models.ManyToManyField(related_name='director_movies', to='movie.directorsactors', verbose_name='Режисер')),
                ('genre', models.ManyToManyField(to='movie.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie.ratingstars')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.movie', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='StillsFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='stills_film', verbose_name='зображения из фильма')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stills_films', to='movie.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильмов',
            },
        ),
    ]