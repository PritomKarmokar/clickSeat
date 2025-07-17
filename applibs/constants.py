from django.db import models

class Languages(models.TextChoices):
    english = 'en', 'English'
    bangla = 'bs', 'Bangla'
    hindi = 'hindi', 'Hindi'