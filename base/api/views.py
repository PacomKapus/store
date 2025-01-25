from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base.models import CreateProduct
from base.api.serializers import CartSerializer, CreateProductSerializer

class CartAPIView(APIView):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []

        for product_id, quantity in cart.items():
            product = CreateProduct.objects.filter(id=product_id).first()
            if product:
                cart_items.append({
                    'product': CreateProductSerializer(product).data,
                    'quantity': quantity
                })

        serializer = CartSerializer({'items': cart_items})
        return Response(serializer.data, status=status.HTTP_200_OK)