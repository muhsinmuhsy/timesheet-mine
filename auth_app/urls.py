from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]