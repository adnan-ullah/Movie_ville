
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductsSerializers


class LatestProduct(APIView):
    def get(self, request, format = None):
        product = Product.objects.all()[0:2]
        serialize = ProductsSerializers(product, many = True)
    
        return Response(serialize.data)
    
class ProductDetails(APIView):
    def get_object(self,category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug= category_slug).get(slug = product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    
    def get(self , request, category_slug, product_slug ,format= None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductsSerializers(product)
        
        return Response(serializer.data)
    
        

