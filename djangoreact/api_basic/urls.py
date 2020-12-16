from django.urls import path
from .views import QuestionAPIView

urlpatterns = [
    path('question-paper/<str:subject>', QuestionAPIView.as_view())
]
