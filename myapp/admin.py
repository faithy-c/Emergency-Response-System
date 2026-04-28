from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'incident_type',
        'status',
        'user',
        'created_at'
    )

    list_filter = (
        'incident_type',
        'status',
        'created_at'
    )

    search_fields = (
        'description',
        'incident_type',
        'user__username'
    )

    ordering = ('-created_at',)

    list_editable = ('status',)