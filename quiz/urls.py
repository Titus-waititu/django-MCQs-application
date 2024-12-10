from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CategoryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', CategoryView)


urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('submit/<int:category_id>/', views.submit_quiz, name='submit_quiz'),
    path('signup/',views.signup, name = 'signup'),
    path('signin/',views.signin, name = 'signin'),
    path('log_out/',views.log_out, name = 'log_out'),
    path('ticket/' , views.ticket, name='ticket'),
    # path('search/' , views.search, name='search'),
    path('delete_account/<id>/' , views.delete_account, name='delete_account'),
    path('deletehist/<id>/' , views.delete, name='deletehist'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('profile/',views.profile, name = 'profile'),
    # path('search/',views.search, name = 'search'),
    path('api/categories', include(router.urls))
    
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
