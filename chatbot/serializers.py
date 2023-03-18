from rest_framework import serializers
from .models import WorkoutPlan, Exercise, Achievement

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'workout_plan', 'sets', 'reps')

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ('id', 'user', 'name', 'description', 'start_date', 'end_date', 'exercises')

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'user', 'name', 'description', 'date_achieved')
