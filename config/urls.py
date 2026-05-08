"""
URL configuration for config project.
"""

from django.contrib import admin                     # Django admin tools
from django.urls import path, include                # URL routing tools

# JWT authentication views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,                             # Login endpoint
    TokenRefreshView,                                # Refresh token endpoint
)

# drf-spectacular views for API documentation
from drf_spectacular.views import (
    SpectacularAPIView,                              # Generates API schema
    SpectacularSwaggerView,                          # Swagger UI page
)

urlpatterns = [

    # Django admin panel
    path(
        'admin/',
        admin.site.urls
    ),

    # Task app routes
    path(
        'api/',
        include('tasks.urls')
    ),

    # Login endpoint
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    # Refresh JWT token endpoint
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Generates OpenAPI schema
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),

    # Swagger documentation UI
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui'
    ),
]