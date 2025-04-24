from django.db import models
from tinymce.models import HTMLField

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = HTMLField()  # campo com formatação estilo Word


class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = HTMLField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/', blank=True)
    project_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title