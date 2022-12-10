from django.http import Http404
# from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response

from base.models import Info_University
from base.serializers import Base_Serializers

class Info_API (APIView):
    def get(self, request, fromat= None):
        info = Info_University.objects.all()
        serializer = Base_Serializers(info, many = True)
        
        return Response(serializer.data)
    
    
class Each_Info(APIView):
    def get_object(self, all_info):
        try:
            return Info_University.objects.get(slug = all_info)
        except Info_University.DoesNotExist:
            raise Http404
        
    
    def get(self , request, info_slug ,format= None):
        info = self.get_object(info_slug)
        serializer = Base_Serializers(info)
        
        return Response(serializer.data)
    