from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('timesheets/', timesheets, name='timesheets')
]