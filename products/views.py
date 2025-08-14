from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['price']
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
            
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
            
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
            
        return queryset
