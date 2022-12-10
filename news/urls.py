

from django.urls import include, path
from . import views
urlpatterns = [
    path('latest-news/',views.LatestNews.as_view()),
    path('news/<slug:category_slug>/<slug:news_slug>/',views.NewsDetails.as_view()),
    path('all-images/',views.All_ImageShows.as_view()),
    path('news-images/<slug:news_slug>/',views.Individual_Images_News.as_view()),
       
]
