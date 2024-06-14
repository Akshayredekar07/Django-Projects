from django.urls import path 
from . import views

urlpatterns = [
    path("attendane/", views.attendance_view),
    path("exam/", views.exam_view),
]