from django import forms
from .models import EmployeeSurvey

class EmployeeSurveyForm(forms.ModelForm):
    class Meta:
        model = EmployeeSurvey
        fields = '__all__'
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'length_of_service': forms.Select(attrs={'class': 'form-control'}),
            'work_environment': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Very satisfied', 'Very satisfied'),
                ('Satisfied', 'Satisfied'),
                ('Neutral', 'Neutral'),
                ('Dissatisfied', 'Dissatisfied'),
                ('Very dissatisfied', 'Very dissatisfied'),
            ]),
            'work_life_balance': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Excellent', 'Excellent'),
                ('Good', 'Good'),
                ('Fair', 'Fair'),
                ('Poor', 'Poor'),
                ('Very poor', 'Very poor'),
            ]),
            'resources': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Yes, always', 'Yes, always'),
                ('Sometimes', 'Sometimes'),
                ('Rarely', 'Rarely'),
                ('No, never', 'No, never'),
            ]),
            # Add similar widgets for all other fields...
            'positives': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'improvements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
