"""
    asosiy urls fayl
"""
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
