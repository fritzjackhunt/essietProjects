from re import template
from django.urls import path

from . import views
from .views import UserRegisterView, UserEditView
#from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]