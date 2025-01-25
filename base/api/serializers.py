from rest_framework import serializers
from base.models import CreateProduct, Blog

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateProduct
        fields = ['id', 'user', 'photo', 'title', 'text', 'price', 'section', 'likes', 'created_at']
    

class CartItemSerializer(serializers.Serializer):
    product = CreateProductSerializer()
    quantity = serializers.IntegerField()

class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)