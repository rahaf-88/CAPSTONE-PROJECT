from django.db import models

# Create your models here.
class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255)  
    answer = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)