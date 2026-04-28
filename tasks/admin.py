from django.contrib import admin     # Import Django admin
from .models import Task             # Import Task model

@admin.register(Task)                # Register Task model with admin panel
class TaskAdmin(admin.ModelAdmin):   # Customize admin display
    list_display = (                 # Fields to show in admin list view
        'id',                        # Task ID
        'title',                     # Task title
        'owner',                     # Task owner
        'status',                    # Task status
        'created_at',                # Creation timestamp
    )