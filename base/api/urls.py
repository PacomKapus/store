from django.urls import path
from .views import CartAPIView

from django.urls import path
from .views import CartAPIView

urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='api_cart'),
]
