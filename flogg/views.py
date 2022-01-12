from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductPostSerializer, ProductGetSerializer
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





