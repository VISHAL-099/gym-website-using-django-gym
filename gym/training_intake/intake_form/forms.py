from django import forms
from .models import ClientIntake

class ClientIntakeForm(forms.ModelForm):
    class Meta:
        model = ClientIntake
        fields = '__all__'
        labels = {
            'full_name': 'Full Name',
            'gender': 'Gender',
            'age': 'Age',
            'height': 'Height (in cm)',
            'weight': 'Weight (in kg)',
            'occupation': 'Occupation',
            'activity_level': 'Activity Level',
            'work_schedule': 'Work Schedule',
            'travel_frequency': 'Travel Frequency',
            'physical_activities': 'Physical Activities',
            'medical_conditions': 'Medical Conditions',
            'medications': 'Medications',
            'therapies': 'Therapies',
            'injuries': 'Injuries',
            'family_diseases': 'Any Family History of Diseases?',
            'smoking_status': 'Do You Smoke?',
            'diet_type': 'Diet Type',
            'fitness_goals': 'Fitness Goals',
            'training_frequency': 'Training Frequency (per week)',
            'preferred_training_time': 'Preferred Training Time',
            'expectations': 'Expectations from Training',
            'agreed_terms': 'Agree to Terms and Conditions',
            'phone_number': 'Phone Number',
            'health_reports': 'Upload Health Reports (if any)',
            'attached_file': 'Attach Additional Files (if any)',
        }
        widgets = {
            'gender': forms.Select(),
            'diet_type': forms.Select(),
            'fitness_goals': forms.Textarea(attrs={'rows': 3}),
            'expectations': forms.Textarea(attrs={'rows': 3}),
            'physical_activities': forms.Textarea(attrs={'rows': 3}),
            'medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'medications': forms.Textarea(attrs={'rows': 3}),
            'therapies': forms.Textarea(attrs={'rows': 3}),
            'injuries': forms.Textarea(attrs={'rows': 3}),
            'diet_type': forms.Textarea(attrs={'rows': 3}),
        }
