from django.urls import path, include, re_path
from . import views

app_name = "query"

urlpatterns = [
    path('', views.CreateQueryView.as_view()),
    path('list/', views.QueryView.as_view()),
    path('answer/', views.AnswerQueryView.as_view()),
    ]
