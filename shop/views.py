from django.http import HttpResponse
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend, FilteringFilterBackend, IdsFilterBackend,
    OrderingFilterBackend, SearchFilterBackend)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from elasticsearch_dsl import Q
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    search_fields = ('title', 'description',)
    filter_fields = {
        "title"

    }
    ordering_fields = {
        'id': 'id',
        'price': 'price',
    }
    ordering = ('id',)


class SearchProduct(APIView, LimitOffsetPagination):

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'title'
                ], fuzziness='auto') & Q(
                    'bool',
                should=[
                    Q('match', is_default=True),
                ], minimum_should_match=1)

            search = ProductDocument.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.ProductDocumentSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)
