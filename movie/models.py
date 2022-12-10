from django.db import models


class MovieData(models.Model):
    title = models.CharField(max_length=100,blank = True, null = True)
    original_title =  models.CharField(max_length=100,blank = True, null = True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.CharField(max_length=100,blank = True, null = True)
    release_date =  models.CharField(max_length=100,blank = True, null = True)
    vote_average = models.CharField(max_length=100,blank = True, null = True)
    vote_count =  models.CharField(max_length=100,blank = True, null = True)
    video = models.BooleanField(null=True,blank = True)
    backdrop_path = models.CharField(max_length=100,blank = True, null = True)
    poster_path = models.CharField(max_length=100,blank = True, null = True)
    slug = models.CharField(max_length=100,blank = True, null = True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
         return f'/subpages/{self.slug}/'  


    

   