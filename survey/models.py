from django.db import models

class EmployeeSurvey(models.Model):
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    length_of_service = models.CharField(max_length=50, choices=[
        ('<1', 'Less than 1 year'),
        ('1-3', '1–3 years'),
        ('3-5', '3–5 years'),
        ('>5', 'More than 5 years'),
    ])
    work_environment = models.CharField(max_length=50)
    work_life_balance = models.CharField(max_length=50)
    resources = models.CharField(max_length=50)
    professional_growth = models.CharField(max_length=50)
    recognition = models.CharField(max_length=50)
    leadership_communication = models.CharField(max_length=50)
    teamwork = models.CharField(max_length=50)
    diversity_inclusion = models.CharField(max_length=50)
    conflict_resolution = models.CharField(max_length=50)
    positives = models.TextField(blank=True, null=True)
    improvements = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Survey by {self.position} in {self.department}"
