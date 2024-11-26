from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('submit/<int:category_id>/', views.submit_quiz, name='submit_quiz'),
     path('signup/',views.signup, name = 'signup'),
    path('signin/',views.signin, name = 'signin'),
    path('log_out/',views.log_out, name = 'log_out'),
     path('ticket/' , views.ticket, name='ticket'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('profile/',views.profile, name = 'profile'),
    
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
