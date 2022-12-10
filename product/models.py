from ctypes.wintypes import RGB
from distutils.command.upload import upload
# from msilib.schema import File
from unicodedata import category
from django.db import models
from matplotlib.image import thumbnail
from io import BytesIO
from PIL import Image

class Category(models.Model):
     name = models.CharField(max_length=250)
     slug = models.SlugField()
     
     class Meta:
         ordering = ('name',)
         
     def __str__(self):
         return self.name
     
     def get_absolute_url(self):
         return f'/{self.slug}/'
     
     
class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to = "uploads/",null = True, blank=True)
    product_thumbnail = models.ImageField(upload_to = "uploads/",null = True, blank=True)
    date_time = models.DateField(auto_now_add=True)
     
    class Meta:
        ordering = ('-date_time',)
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
         return f'/{self.category.slug}/{self.slug}/'  
       
    def get_image(self):
        if self.product_image:
            return f'http://127.0.0.1:8000' + self.product_image.url
        return ''
    
    def get_thumbnail(self):
        
        if self.product_thumbnail:
            return f'http://127.0.0.1:8000' + self.product_thumbnail.url
        
        else:
            if self.product_image:
                self.product_thumbnail = self.make_thumbnail(self.product_image)
                return  f'http://127.0.0.1:8000' + self.product_thumbnail.url
            return ''
    
    def make_thumbnail(self, image , size =(200,300)):
        img = Image.open(image)
        img = img.convert(RGB)
        
        img.thumbnail(size)
        
        thubmnail = BytesIO()
        img.save(thubmnail, 'JPG', quality =85)
      ##  pr_thumbnail = File(img,name= image.name)
        
        return 1