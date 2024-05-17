from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='members'),
    path('new_note/', views.new_notes, name='new notes'),
    path('all_notes/', views.all_notes, name='all notes'),
]