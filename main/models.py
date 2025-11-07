from django.db import models
from ckeditor.fields import RichTextField
#this is best tha ol way

from django.db import models

class Service(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    #image = models.ImageField(upload_to='services/', blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, default='services/default.jpg')

    # icone = models.CharField(max_length=100, blank=True)  # ex: 🚿 ou fa-solid fa-bath  # ex: 🚿 ou fa-solid fa-bath

    def __str__(self):
        return self.titre



class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    texte = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service.titre} - {self.texte}"




class Project(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/')

    date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

class Testimonial(models.Model):
    nom = models.CharField(max_length=100)
    contenu = models.TextField()
    note = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f"{self.nom} ({self.note})"

class ContactRequest(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact: {self.nom} - {self.email}"
