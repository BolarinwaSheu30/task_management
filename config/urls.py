"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # import URL tools

from rest_framework import permissions # import permissions
from drf_yasg.views import get_schema_view # Function to generate Swagger schema
from drf_yasg import openapi  # OpenAPI tools for API metadata

from rest_framework_simplejwt.views import(
    TokenObtainPairView,             #Login + get tokens
    TokenRefreshView,               #Refresh access token
)

# Configure Swagger schema
schema_view = get_schema_view(
    openapi.Info(                                         # API metadata
        title="Task Management API",                      # API name shown in docs
        default_version='v1',                             # Version
        description="API for managing tasks",             # Description
    ),
    public=True,                                          # Make docs public
    permission_classes=[permissions.AllowAny],            # Anyone can view docs
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route

    path('api/', include('tasks.urls')), # Include task routes under /api/

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh endpoint

    # Swagger UI (interactive API docs)
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # Optional alternative docs UI
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='redoc'),
]
