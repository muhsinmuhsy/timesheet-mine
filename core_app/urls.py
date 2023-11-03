from django.urls import path
from core_app.views import *

urlpatterns = [
    path('', index, name='index')
]