\
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.retrive_view),
    path("aggregate/", views.aggregate_view),

]
