from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product,Category
from rest_framework.response import Response
from apiApp.serializers import ProductListSerializer,ProductDetailSerializer,CategoryListSerializer,CategoryDetailSerializer

# Create your views here.


@api_view(['GET'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, slug):
    products = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(products)
    return Response(serializer.data)


@api_view(["GET"])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def category_detail(request,slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)