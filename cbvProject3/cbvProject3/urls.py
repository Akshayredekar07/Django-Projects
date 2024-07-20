
from django.contrib import admin
from django.urls import path
from durga import views

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", views.CompanyListView.as_view(), name='list'),
    path("<int:pk>", views.CompanyDetailView.as_view(), name='detail'),
    path("<int:pk>", views.CompanyDetailView.as_view()),
    path("create/", views.CompanyCreateView.as_view()),
    path("update/<int:pk>", views.CompanyUpdateView.as_view()),
    path("delete/<int:pk>", views.CompanyDeleteView.as_view()),
]
