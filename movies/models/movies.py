import ulid

from django.db import models
from django.utils import timezone
from applibs.constants import Languages

class Genre(models.Model):
    id = models.CharField(max_length=26, primary_key=True, editable=False)
    title = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'genres'
        verbose_name = 'Genre'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ulid.new().__str__()
        super().save(*args, **kwargs)

class Movie(models.Model):
    id = models.CharField(max_length=26, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='movies')
    released_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    lang = models.CharField(
        max_length=10,
        choices=Languages.choices,
        default=Languages.english
    )

    class Meta:
        db_table = 'movies'
        verbose_name = 'Movie'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ulid.new().__str__()
        super().save(*args, **kwargs)