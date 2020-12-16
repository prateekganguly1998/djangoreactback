from django.db import models

# Create your models here.

class Question(models.Model):
    subject=models.CharField(max_length=20)
    difficulty=models.CharField(max_length=20,default="EASY")
    question=models.TextField()
    options=models.JSONField()
    answer=models.TextField()

    def __str__(self):
        return self.question
    
