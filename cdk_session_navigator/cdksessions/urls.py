# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cdksessions/', views.session_list, name='session_list'),
]
