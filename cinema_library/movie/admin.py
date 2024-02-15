from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(DirectorsActors)
class DirectorsActorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(StillsFilm)
class StillsFilmAdmin(admin.ModelAdmin):
    pass


@admin.register(RatingStars)
class RatingStarsAdmin(admin.ModelAdmin):
    pass




@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
