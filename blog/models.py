from django.db import models
from django.utils import timezone
# Create your models here.

# Модель блогу (постів)
class BlogModel(models.Model):
    title = models.CharField(max_length=200) # заголовок
    date = models.DateField(auto_now=True) # дата створення
    description = models.TextField() # опис

    def __str__(self):
        return self.title
