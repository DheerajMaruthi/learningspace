from django.urls import path, include, re_path
from .views import RegisterAPIView

app_name= "account"

urlpatterns = [
     path('register/', RegisterAPIView.as_view(), name='register'),
     ]
