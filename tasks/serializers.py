from rest_framework import serializers                      # Import DRF serializer tools
from .models import Task                                    # Import Task model
from django.contrib.auth.models import User                 # Import Django User model
from django.contrib.auth.password_validation import validate_password  # Import password validators


class TaskSerializer(serializers.ModelSerializer):          # Serializer for Task model
    """
    Converts Task model ↔ JSON
    """

    class Meta:                                             # Configuration class
        model = Task                                        # Use Task model
        fields = '__all__'                                  # Include all fields
        read_only_fields = ['owner']                        # Prevent manual owner input


class UserRegisterSerializer(serializers.ModelSerializer):  # Serializer for user registration

    email = serializers.EmailField(                         # Add email field
        required=True                                       # Make email required
    )

    password = serializers.CharField(                       # Password field
        write_only=True,                                    # Do not return in response
        required=True,                                      # Must be provided
        validators=[validate_password]                      # Apply Django password validation
    )

    class Meta:                                             # Meta config
        model = User                                        # Use User model
        fields = ['id', 'username', 'email', 'password']     # Include email now

    def validate_email(self, value):                         # Custom email validation
        """
        Ensure email is unique.
        """
        if User.objects.filter(email=value).exists():        # Check if email already exists
            raise serializers.ValidationError("Email already in use")  # Raise error
        return value                                         # Return valid email

    def validate_username(self, value):                      # Custom username validation
        """
        Ensure username is unique.
        """
        if User.objects.filter(username=value).exists():     # Check if username exists
            raise serializers.ValidationError("Username already taken")  # Raise error
        return value                                         # Return valid username

    def create(self, validated_data):                        # Override create method
        """
        Create user with hashed password.
        """
        user = User.objects.create_user(                     # Use create_user for hashing
            username=validated_data['username'],             # Set username
            email=validated_data['email'],                   # Set email
            password=validated_data['password']              # Hash password automatically
        )
        return user                                          # Return created user