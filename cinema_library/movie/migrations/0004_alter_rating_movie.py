# Generated by Django 5.0.1 on 2024-02-15 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_rating_rating_delete_ratingstars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_movies', to='movie.movie'),
        ),
    ]
