from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


# app_name = "student_app"


urlpatterns = [
    path('', login_required(views.Home.as_view()) ,name='home'),
    
]