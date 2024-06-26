from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, ProductDocumentViewSet, ProductViewSet,
                    SearchProduct)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'search', ProductDocumentViewSet, basename="search_product")

urlpatterns = [
    path('', include(router.urls)),
    path('search/<str:query>/', SearchProduct.as_view())
]
