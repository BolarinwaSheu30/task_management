


from django.db.models import Q                          # Import Q for complex queries
from rest_framework import viewsets, generics,status           # Import DRF viewsets,generic views and status codes
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import permissions
from .models import Task                                # Import Task model
from .serializers import TaskSerializer, UserRegisterSerializer  # Import serializers
from django.contrib.auth.models import User             # Import User model

from rest_framework.response import Response            #import response class
from drf_yasg.utils import swagger_auto_schema # Import Swagger decorator
from .permissions import IsOwner     # Import custom permission


class TaskViewSet(viewsets.ModelViewSet):               # ModelViewSet gives full CRUD
    """
    Handles:
    - list
    - create
    - retrieve
    - update
    - delete
    """

    serializer_class = TaskSerializer                   # Use Task serializer
    permission_classes = [IsAuthenticated, IsOwner]              # Require authentication

    def get_queryset(self):                             # MUST be inside the class
        """
        Return filtered tasks for the logged-in user.
        Supports:
        - filtering by status
        - searching by title and description
        """

        queryset = Task.objects.filter(                 # Start with user's tasks
            owner=self.request.user                     # Only return user's tasks
        )

        status = self.request.query_params.get('status')  # Get status from query params
        search = self.request.query_params.get('search')  # Get search keyword

        if status:                                      # If status is provided
            queryset = queryset.filter(                 # Filter by status
                status=status
            )

        if search:                                      # If search is provided
            queryset = queryset.filter(                 # Apply search filter
                Q(title__icontains=search) |            # Search in title
                Q(description__icontains=search)        # OR search in description
            )

        return queryset                                 # Return final queryset

    def perform_create(self, serializer):               # Keep your create logic
        """
        Automatically assign logged-in user as owner
        """
        serializer.save(
            owner=self.request.user                     # Assign current user
        )
    @swagger_auto_schema(                                  # Tell Swagger how this endpoint behaves
        operation_description="Create a new task",         # Description shown in Swagger UI
        request_body=TaskSerializer,                      # Define expected request body structure
        responses={201: TaskSerializer}                   # Define response format
    )
    def create(self, request, *args, **kwargs):            # Override default create method
        """
        Create a new task and assign it to the logged-in user
        """

        serializer = self.get_serializer(                 # Initialize serializer with request data
            data=request.data                            # Incoming JSON data
        )

        serializer.is_valid(raise_exception=True)         # Validate input data

        self.perform_create(serializer)                   # Call your existing logic (assign owner)

        return Response(                                 # Return HTTP response
            serializer.data,                             # Return created object data
            status=status.HTTP_201_CREATED               # Status code 201 = created
        )
    


class UserRegisterView(generics.CreateAPIView):         # Registration view
    """
    Allows new users to register.
    """

    queryset = User.objects.all()                       # Required queryset
    serializer_class = UserRegisterSerializer           # Use registration serializer
    permission_classes = [AllowAny]                     # Public endpoint