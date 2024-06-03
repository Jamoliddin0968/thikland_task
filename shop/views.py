from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend, OrderingFilterBackend, SearchFilterBackend)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shop.documents import ProductDocument

from .models import Category, Product
from .serializers import (CategorySerializer, ProductDocumentSerializer,
                          ProductSerializer)


@extend_schema_view(
    list=extend_schema(tags=['Category']),
    retrieve=extend_schema(tags=['Category']),
    create=extend_schema(tags=['Category']),
    update=extend_schema(tags=['Category']),
    partial_update=extend_schema(tags=['Category']),
    destroy=extend_schema(tags=['Category']),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(tags=['Product']),
    retrieve=extend_schema(tags=['Product']),
    create=extend_schema(tags=['Product']),
    update=extend_schema(tags=['Product']),
    partial_update=extend_schema(tags=['Product']),
    destroy=extend_schema(tags=['Product']),
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Получение списка продуктов",
        parameters=[
            OpenApiParameter(name='search', description='Поиск по названию и описанию',
                             type=OpenApiTypes.STR, required=False),
            OpenApiParameter(name='title', description='Фильтр по названию продукта',
                             type=OpenApiTypes.STR, required=False),
            OpenApiParameter(name='ordering', description='Сортировка списка продуктов',
                             type=OpenApiTypes.STR, required=False),
        ]
    ),
    retrieve=extend_schema(
        description="Получение детальной информации о продукте",
        parameters=[
            OpenApiParameter(name='id', description='Уникальный идентификатор продукта для поиска',
                             type=OpenApiTypes.INT, required=True)
        ]
    ),
)
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
