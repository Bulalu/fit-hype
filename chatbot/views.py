from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import WorkoutPlan, Exercise, Achievement
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, AchievementSerializer

from rest_framework import views, response
from .openai_bot import chat_with_gpt3

class GPT3BotView(views.APIView):
    def post(self, request):
        user_input = request.data.get("user_input", "")
        if not user_input:
            return response.Response({"error": "User input is required."}, status=400)

        gpt3_response = chat_with_gpt3(user_input)
        return response.Response({"gpt3_response": gpt3_response})

class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseListCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    def get_object(self):
        return get_object_or_404(WorkoutPlan, pk=self.kwargs['pk'], user=self.request.user)
