from django.shortcuts import render
import requests



import coreapi
import io

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import Http404, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MovieData
from .serializers import MovieSerializers



import json

@csrf_exempt
def movieApi(request):
    if request.method == "GET":
       
        
        

        
        
        
        movies_data = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=6e63c2317fbe963d76c3bdc2b785f6d1&page=1').json()
        
        
        datalist = movies_data['results']
        for i in datalist:
            movie_info = MovieData(
                title = i['title'],
                original_title = i['original_title'],
                overview = i['overview'],
                popularity = i['popularity'],
                release_date = i['release_date'],
                vote_average = i['vote_average'],
                vote_count = i['vote_count'],
                video = i['video'],
                backdrop_path = i['backdrop_path'],
                poster_path = i['poster_path'],
                slug = i['id']
              
               
            )
            movie_info.save()
            movie_result = MovieData.objects.all().order_by('-id')


        print(datalist)
        #movie_info = MovieData.create(attr=movies_data['results'])
        
        # print(movies_data['results'])
        # movieSerializer = MovieSerializers(data=movies_data['results'], many=True)
        movieSerializer = MovieSerializers(data= movie_result, many=True)
        
        if movieSerializer.is_valid():
            print("True Argentina")
            movieSerializer.save()
            
            return JsonResponse(movieSerializer.data, safe=False)
        ##return JsonResponse("Failed to Add", safe=False)
        else:
            movieSerializer.save()
            return JsonResponse(movieSerializer.data, safe=False)
      

    elif request.method== "POST":
        movies_data = JSONParser().parse(requests.get('https://api.covid19api.com/countries').json())
        movieSerializer = MovieSerializers(data = movies_data)
        if movieSerializer.is_valid():
            movieSerializer.save()
            return JsonResponse("ADDED SUCCESSFULLY", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def latestMovie( request):
        movies = MovieData.objects.all()[0:4]
        serialize = MovieSerializers(movies, many = True)
    
        return JsonResponse(serialize.data, safe=False)



class MovieDetails(APIView):
    def get_object(self,slug):
        try:
            
            return MovieData.objects.filter(slug = slug)
        except MovieData.DoesNotExist:
            raise Http404
        
    
    def get(self , request, slug ,format= None):
        movie = self.get_object(slug)
        serializer = MovieSerializers(movie, many=True)
        return Response(serializer.data)
    