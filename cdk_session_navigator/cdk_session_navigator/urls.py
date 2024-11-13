from django.contrib import admin
from django.urls import path
from sessions import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sessions/', views.session_list, name='session_list'),
]