from django.urls import path 
# from testapp import views
from . import views

urlpatterns = [
    path('', views.index_view),
    # path('movies/', views.movies_view)
    path('movies/', views.movies_view, name='movies'),
    path('sports/', views.sports_view, name='sports'),
    path('politics/', views.politics_view, name='politics'),
]

