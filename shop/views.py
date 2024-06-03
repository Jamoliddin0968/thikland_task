from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend, OrderingFilterBackend, SearchFilterBackend)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shop.documents import ProductDocument

from .models import Category, Product
from .serializers import (CategorySerializer, ProductDocumentSerializer,
                          ProductSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
        OrderingFilterBackend,
    ]
    search_fields = ('title', 'description',)
    filter_fields = {
        "title": {"field": "title"}
    }
    ordering_fields = {
        'id': 'id',
        'price': 'price',
    }
    ordering = ('id',)
