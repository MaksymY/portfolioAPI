from django.db import models

class Project(models.Model): 
    title = models.CharField(max_length=50)
    img = models.ImageField(blank=True)
    description = models.TextField()