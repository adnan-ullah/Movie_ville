from rest_framework import serializers


from base.models import Info_University

class Base_Serializers(serializers.ModelSerializer):
    class Meta:
        model  =  Info_University
        
        fields = (
            "id",
            "title",
            "description",
            "slug",
            "get_image",
            "get_absolute_url"
            
        )