from django.contrib import admin
from .models import Category, Question, Answer,UserQuizHistory,Testimonial,Ticket

# Register your models here.
class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Testimonial)
admin.site.register(Ticket)
admin.site.register(UserQuizHistory)



