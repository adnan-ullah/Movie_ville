
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import News , ImageList_News
from .serializers import NewsSerializers , NewsImageSerializer


class LatestNews(APIView):
    def get(self, request, format = None):
        news = News.objects.all()[0:4]
        serialize = NewsSerializers(news, many = True)
    
        return Response(serialize.data)
    
class NewsDetails(APIView):
    def get_object(self,category_slug, news_slug):
        try:
            return News.objects.filter(category__slug= category_slug).get(slug = news_slug)
        except News.DoesNotExist:
            raise Http404
        
    
    def get(self , request, category_slug, news_slug ,format= None):
        news = self.get_object(category_slug, news_slug)
        serializer = NewsSerializers(news)
        
        return Response(serializer.data)
    

class All_ImageShows(APIView):
    def get(self, request, format = None):
        images = ImageList_News.objects.all()[0:4]
        serialize = NewsImageSerializer(images, many = True)
        return Response(serialize.data)

   
class Individual_Images_News(APIView):
    def get(self , request, news_slug ,format= None):
        img = ImageList_News.objects.filter(parent__slug = news_slug)
        serializer = NewsImageSerializer(img, many = True)
        
        return Response(serializer.data)