from django.db import models
from django.contrib.auth.models import User


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    description = models.TextField()

    latitude = models.FloatField()
    longitude = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_incident_type_display()} - {self.user.username}"