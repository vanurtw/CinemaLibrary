# Generated by Django 5.0.1 on 2024-02-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_alter_reviews_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=5, max_length=20, verbose_name='Рейтинг'),
        ),
    ]
