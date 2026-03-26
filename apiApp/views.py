from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from .models import Product,Category,Cart,CartItem,Review
from rest_framework.response import Response
from apiApp.serializers import ProductListSerializer,ProductDetailSerializer,CategoryListSerializer,CategoryDetailSerializer,CartSerializer,CartItemSerializer,ReviewSerializer

# Create your views here.
User = get_user_model()


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

@api_view(["POST"])
def add_to_cart(request):
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity")


    cart , created = Cart.objects.get_or_create(cart_code=cart_code)
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity = 1
    cart_item.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["PUT"])
def update_cartitem_quantity(request):
    cartitem_id = request.data.get("item_id")
    quantity = request.data.get("quantity")

    quantity = int(quantity)

    cartitam = CartItem.objects.get(id = cartitem_id)
    cartitam.quantity = quantity
    cartitam.save()

    serializer = CartItemSerializer(cartitam)
    return Response({"data":serializer.data, "message":"Cartitem Updated Succesfully!"})


@api_view(["POST"])
def add_review(request):
    product_id = request.data.get("product_id")
    email = request.data.get("email")
    rating = request.data.get("rating")
    review = request.data.get("review")

    product = Product.objects.get(id=product_id)
    user = User.objects.get(email=email)

    review = Review.objects.create(product=product,user=user,rating=rating,review=review)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)