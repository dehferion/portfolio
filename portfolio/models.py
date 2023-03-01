from django.db import models

# Create your models here.

# модель виконаних проектів
class Project(models.Model):
    title = models.CharField(max_length=100) # заголовок
    description = models.CharField(max_length=255) # опис
    image = models.ImageField(upload_to='portfolio/images/') # зображення
    url = models.URLField(blank=True)  # посилання

    def __str__(self):
        return self.title
