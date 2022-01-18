from rest_framework.serializers import ModelSerializer
from flogg.models import Product, Category, Brand, Detail
from rest_framework import serializers




class ProductGetSerializer(ModelSerializer):

    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    detail = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = ["name", "category", "brand", "color", "price", "weight", "detail"]



class CategorySerializer(serializers.ModelSerializer):
    products = ProductGetSerializer(source="product_set", many=True)
    class Meta:
        model = Category
        fields = ("name", "products")

class BrandSerializer(serializers.ModelSerializer):

    products = ProductGetSerializer(source="product_set", many=True)

    class Meta:
        model = Brand
        fields = ("name", "products")


class DetailSerializer(serializers.ModelSerializer):

    products = ProductGetSerializer(source="product_set", many=True)

    class Meta:
        model = Detail
        fields = ("__all__")


class ProductPostSerializer(ModelSerializer):
    
    category = CategorySerializer(many=False)
    brand = BrandSerializer()
    detail = DetailSerializer()

    class Meta:
        model = Product
        fields = ["name", "price", "category", "brand", "detail"]

    def create(self, validated_data):
        print("you came  here")
        category = validated_data.pop("category")
        brand = validated_data.pop("brand")
        detail = validated_data.pop("detail")
        print("category ->", category)
        print("brand ->", brand)
        print("detail ->", detail)
        try:
            category, _ = Category.objects.get_or_create(**category)
            brand, _ = Brand.objects.get_or_create(**brand)
            detail, _ = Detail.objects.get_or_create(**detail)
        except ValueError:
            return ValueError("error")

        print("category ->", category)
        print("brand ->", brand)
        print("detail ->", detail)

        product = Product(**validated_data, category=category, brand=brand, detail=detail)
        return product
        
    
        





    