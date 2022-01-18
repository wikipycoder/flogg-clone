from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, Category, Brand, Detail
from .serializers import ProductPostSerializer, ProductGetSerializer, CategorySerializer, BrandSerializer, DetailSerializer
from rest_framework.response import Response
from rest_framework import status



class ProductAPIView(APIView):

    def get(self, request):
        
        products = Product.objects.all()
        serializer = ProductGetSerializer(products, many=True)
        return Response(serializer.data)
    

    def post(self, request):

        serializer = ProductPostSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            product.user = request.user
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class BrandAPIView(APIView):

    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    
class DetailAPIView(APIView):

    def get(self, request):
        details = Detail.objects.all()
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)