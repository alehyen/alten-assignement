from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer