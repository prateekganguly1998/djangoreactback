from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
# Create your views here.


#class based views using APIView
class QuestionAPIView(APIView):
    #authentication_classes=[SessionAuthentication,BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,subject):
        questions=Question.objects.filter(subject=subject)
        serializer=QuestionSerializer(questions,many=True)
        #shuffle logic
        easy_questions=[question for question in serializer.data if question['difficulty']=='EASY']
        random.shuffle(easy_questions)
        medium_questions=[question for question in serializer.data if question['difficulty']=='MEDIUM']
        random.shuffle(medium_questions)
        hard_questions=[question for question in serializer.data if question['difficulty']=='HARD']
        random.shuffle(hard_questions)
        questions_paper=easy_questions[:4]+medium_questions[:12]+hard_questions[:4]
        random.shuffle(questions_paper)
        #logic end
        return Response(questions_paper,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=QuestionSerializer(data=request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


