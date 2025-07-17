from django.contrib import admin

from movies.models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'released_year',
        'is_active',
    )

    ordering = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)