# Generated by Django 5.0.1 on 2024-02-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_ratingstars_remove_rating_rating_rating_rating_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingstars',
            name='rating',
            field=models.CharField(max_length=10, verbose_name='Рейтинг'),
        ),
    ]
