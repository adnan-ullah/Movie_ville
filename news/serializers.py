
from attr import field
from rest_framework import serializers

from news.models import News, ImageList_News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "headline",
            "description",
            "slug",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =ImageList_News
        
        fields = (
            "id",
            "parent",
            "get_NewsImage"
            
        )