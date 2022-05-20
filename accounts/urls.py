from unicodedata import name
from django.urls import path
from .views import *
app_name = 'accounts'

urlpatterns = [
    path('',UserAPI.as_view(),name='users')
]