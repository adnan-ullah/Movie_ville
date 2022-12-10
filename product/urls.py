

from django.urls import include, path
from product import views
urlpatterns = [
    path('latest-products/',views.LatestProduct.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetails.as_view()),
       
]
