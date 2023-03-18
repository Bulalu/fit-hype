from django.db import models
from django.contrib.auth.models import User

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_achieved = models.DateField()

    def __str__(self):
        return self.name
