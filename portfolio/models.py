from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blanf=True - не обов'язкове поле

    def __str__(self):
        return self.title
