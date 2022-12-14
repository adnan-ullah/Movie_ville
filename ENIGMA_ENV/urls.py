
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls') ),
    path('api/v1/', include('djoser.urls.authtoken') ),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('news.urls')),
     path('api/v1/', include('base.urls')),
     path('', include('movie.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
