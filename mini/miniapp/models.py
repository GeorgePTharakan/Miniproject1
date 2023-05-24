from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    phone_number = models.CharField(max_length=20)
    email_id = models.EmailField()
    age = models.PositiveIntegerField()
    # Add more fields as needed

class Course(models.Model):
    name = models.CharField(max_length=100)
    #description = models.TextField()
    #instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    #start_date = models.DateField()
   # end_date = models.DateField()
    subject = models.CharField(max_length=100)
    subject_links = models.URLField()
    difficulty_level = models.CharField(max_length=50)
    # Add more fields as needed

class QuestionBank(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    # Add more fields as needed

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)
    time_taken = models.DurationField()

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)
    time_taken = models.DurationField()
    # Add more fields as needed