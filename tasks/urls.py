from rest_framework.routers import DefaultRouter   # Router auto-generates URLs
from .views import TaskViewSet, UserRegisterView                     # Import view & viewset

from django.urls import path    # Import path for manual routes


router = DefaultRouter()                           # Create a router instance
router.register(                                   # Register our viewset
    r'tasks',                                      # URL prefix → /tasks/
    TaskViewSet,                                   # The view handling requests
    basename='task'                                # Base name for URL patterns
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),  # Signup endpoint
]

urlpatterns += router.urls                          # Append router- generated routes