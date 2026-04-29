from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Incident(models.Model):

    INCIDENT_TYPES = [
        ('fire', 'Fire'),
        ('accident', 'Accident'),
        ('crime', 'Crime'),
        ('medical', 'Medical'),
        ('emergency', 'Emergency'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    description = models.TextField()

    latitude = models.FloatField()
    longitude = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    time = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    bool = models.BooleanField(default=False)

    def __str__(self):
      username = self.user.username if self.user else "Anonymous"
      return f"{self.get_incident_type_display()} - {username}"