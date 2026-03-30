from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-appearance/', views.edit_appearance, name='edit_appearance'),
]