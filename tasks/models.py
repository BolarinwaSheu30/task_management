from django.db import models                          # Import Django's model system
from django.contrib.auth.models import User          # Import built-in User model

class Task(models.Model):                             # Define a new model called Task
    """
    This model represents a task created by a user.
    Each instance = one task in the database.
    """

    STATUS_CHOICES = [                                # Predefined choices for task status
        ('pending', 'Pending'),                       # Task not started
        ('in_progress', 'In Progress'),               # Task currently being worked on
        ('completed', 'Completed'),                   # Task finished
    ]

    owner = models.ForeignKey(                        # Create a relationship to the User model
        User,                                         # The model we are linking to
        on_delete=models.CASCADE,                     # Delete tasks if the user is deleted
        related_name='tasks'                          # Allows access via user.tasks
    )

    title = models.CharField(                         # Short text field for task title
        max_length=255                                # Maximum length of 255 characters
    )

    description = models.TextField(                   # Longer text field for details
        blank=True                                    # Optional field (can be empty)
    )

    status = models.CharField(                        # Field to store task status
        max_length=20,                                # Max length for the status string
        choices=STATUS_CHOICES,                       # Restrict values to predefined choices
        default='pending'                             # Default value when task is created
    )

    created_at = models.DateTimeField(                # Field to store when task was created
        auto_now_add=True                             # Automatically set when object is created
    )

    updated_at = models.DateTimeField(                # Field to store last update time
        auto_now=True                                 # Automatically updates on every save
    )

    def __str__(self):                                # String representation of the model
        return self.title                             # What shows in admin panel