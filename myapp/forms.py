from django import forms
from .models import Incident

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'location_building', 'location_room', 'description']
        widgets = {
            'incident_type': forms.Select(attrs={'class': 'form-control'}),
            'location_building': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Wilson Hall'}),
            'location_room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'What happened?'}),
        }
    
    anonymous = forms.BooleanField(required=False, label="Report anonymously")