from ctypes.wintypes import RGB
from distutils.command.upload import upload
# from msilib.schema import File
from unicodedata import category
from django.db import models
from matplotlib.image import thumbnail
from io import BytesIO
from PIL import Image
from sympy import re
from urllib3 import Retry

class News_Category(models.Model):
     name = models.CharField(max_length=250)
     slug = models.SlugField()
     
     class Meta:
         ordering = ('name',)
         
     def __str__(self):
         return self.name
     
     def get_absolute_url(self):
         return f'/{self.slug}/'
     
     
class News(models.Model):
    headline = models.CharField(max_length=250)
    category = models.ForeignKey(News_Category, related_name='news', on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    news_image = models.ImageField(upload_to = "uploads/",null = True, blank=True)
    news_thumbnail = models.ImageField(upload_to = "uploads/",null = True, blank=True)
    date_time = models.DateField(auto_now_add=True)

     
    class Meta:
        ordering = ('-date_time',)
    def __str__(self):
        return self.headline
        
    def get_absolute_url(self):
         return f'/subpages/{self.category.slug}/{self.slug}/'  
       
    def get_image(self):
        if self.news_image:
            return f'http://127.0.0.1:8000' + self.news_image.url
        return ''
    
    def get_thumbnail(self):
        
        if self.news_thumbnail:
            return f'http://127.0.0.1:8000' + self.news_thumbnail.url
        
        else:
            if self.news_image:
                self.news_thumbnail = self.make_thumbnail(self.news_image)
                return  f'http://127.0.0.1:8000' + self.news_thumbnail.url
            return ''
    
    def make_thumbnail(self, image , size = {200,300}):
        img = Image.open(image)
        img = img.convert(RGB)
        
        img.thumbnail(size)
        
        thubmnail = BytesIO()
        img.save(thubmnail, 'JPG', quality =85)
        pr_thumbnail = File(img,name= image.name)
        
        return pr_thumbnail
    
    
    
    
class ImageList_News(models.Model):
    parent = models.ForeignKey(News, related_name='news', on_delete=models.CASCADE)
    news_image_all = models.ImageField(upload_to = "uploads/",null = True, blank=True)
    slug= models.SlugField()
    
    def __str__(self):
        return self.parent.headline
    
    
    def get_NewsImage(self):
        if self.news_image_all:
            return f'http://127.0.0.1:8000' + self.news_image_all.url
        return ''
    
    