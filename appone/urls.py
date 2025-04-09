from django.urls import path
from . import views

urlpatterns = [
    path('', views.snow, name='snow'),
    path('one/', views.one, name='one'),
]
