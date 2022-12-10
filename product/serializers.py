
from rest_framework import serializers

from product.models import Product ,Category


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "description",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )