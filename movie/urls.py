from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
##import Usersapi.viewsets as viewset
from . import views

router = routers.DefaultRouter()
##router.register('usersapi', viewset.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('movie/', views.movieApi),
    path('latest_movie/', views.latestMovie),
    path('movie/<slug:slug>/',views.MovieDetails.as_view()),
    
]