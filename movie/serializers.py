from rest_framework import serializers
from .models import MovieData

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ('title','original_title','overview','popularity','release_date','vote_average','vote_count','video','backdrop_path','poster_path','get_absolute_url','slug')

        
    