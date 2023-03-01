# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("",views.login_view,name="login"),
    path('register/', views.register_view, name='register'),
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]