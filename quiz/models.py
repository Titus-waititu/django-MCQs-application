import uuid
from django.conf import settings
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    pass1 = models.CharField(max_length=500)
    pass2 = models.CharField(max_length=500)

    def __str__(self):
        return self.username
  

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    
    class Meta:
        abstract = True
        
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    total_marks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

class Ticket(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.full_name

class Testimonial(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
# add model to capture user quiz history
class UserQuizHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Dynamically reference User model
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    total_marks = models.PositiveIntegerField(default=0)
    percentage = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.score}/{self.total_marks} - {self.percentage}%"