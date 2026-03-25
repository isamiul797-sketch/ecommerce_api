from rest_framework import serializers
from .models import Product,Category,Cart,CartItem


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ["id","name","slug","price","image"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ["id","name","slug","description","price","image"]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","image","slug"]

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ["id","name","image","products"]

class CartItemSerializer(serializers.ModelSerializer):
    Product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id","product","quantity","sub_total"]


    def get_sub_total(self,cartitem):
        total = cartitem.quantity * cartitem.product.price
        return total
    

class CartSerializer(serializers.ModelSerializer):
    cartitem = CartItemSerializer(many=True,read_only=True)
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id","cart_code","cartitems","cart_total"]

    def get_cart_total(self,cart):
        items = cart.cartitem.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
    
class cartStatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id","cart_code","total_quantity"]

    def get_total_products(self,cart):
        items = cart.cartitem.all()
        total = sum([item.quantity for item in items])
        return total


