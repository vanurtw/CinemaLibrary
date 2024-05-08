# Generated by Django 5.0.1 on 2024-02-17 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='movie.ratingstars', verbose_name='Рейтинг'),
        ),
    ]