from django.db import models


class ClientIntake(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    occupation = models.CharField(max_length=255)
    activity_level = models.CharField(max_length=50)
    work_schedule = models.CharField(max_length=50)
    travel_frequency = models.CharField(max_length=50)
    physical_activities = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    therapies = models.TextField(blank=True, null=True)
    injuries = models.TextField(blank=True, null=True)
    family_diseases = models.BooleanField()
    smoking_status = models.BooleanField()
    diet_type = models.CharField(max_length=50)
    fitness_goals = models.TextField()
    training_frequency = models.IntegerField()
    preferred_training_time = models.CharField(max_length=50)
    expectations = models.TextField()
    agreed_terms = models.BooleanField()
    phone_number = models.CharField(max_length=15)
    health_reports = models.FileField(upload_to='health_reports/', blank=True, null=True)
    attached_file = models.FileField(upload_to='attached_files/', blank=True, null=True)

    def __str__(self):
        return self.full_name
