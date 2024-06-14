from django.urls import path 
from . import views

urlpatterns = [
    path("first/", views.first_view),
    path("sec/", views.second_view),
    path("third/", views.third_view),
    path("four/", views.four_view),
    path("fifth/", views.fifith_view),
]