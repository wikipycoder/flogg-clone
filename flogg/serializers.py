from rest_framework.serializers import ModelSerializer
from flogg.models import Product, Category, Brand, Detail
from rest_framework import serializers


class ProductPostSerializer(ModelSerializer):


    class Meta:
        model = Product
        fields = ["name", "price", "category", "brand", "detail"]

    def create(self, validated_data):

        category = validated_data.pop("category")
        brand = validated_data.pop("brand")
        detail = validated_data.pop("detail")

        category = Category.objects.get_or_create(**category)
        brand = Brand.objects.get_or_create(**brand)
        detail = Detail.objects.get_or_create(**detail)

        product = Product(**validated_data, category=category, brand=brand, detail=detail)
        return product
        
    
        

class ProductGetSerializer(ModelSerializer):

    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    detail = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = ["name", "price", "category", "brand", "detail"]





    