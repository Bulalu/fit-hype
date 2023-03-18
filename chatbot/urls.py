from django.urls import path
from . import views

urlpatterns = [
    path('workout_plans/', views.WorkoutPlanListCreateView.as_view(), name='workout_plan_list_create'),
    path('workout_plans/<int:pk>/', views.WorkoutPlanRetrieveUpdateDestroyView.as_view(), name='workout_plan_retrieve_update_destroy'),
    path('exercises/', views.ExerciseListCreateView.as_view(), name='exercise_list_create'),
    path('gpt3_bot/', views.GPT3BotView.as_view(), name='gpt3_bot'),

    # Add more URL patterns for other views as needed
]
