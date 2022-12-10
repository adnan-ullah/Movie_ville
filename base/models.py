from distutils.command.upload import upload
from django.db import models
from sqlalchemy import null, true
from tables import Description

class Info_University(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    slug = models.SlugField()
    image = models.ImageField( upload_to="uploads/", blank= True, null=True) 
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return f'http://127.0.0.1:8000' + self.image.url   
        return ''
    