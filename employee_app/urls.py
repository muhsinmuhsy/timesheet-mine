from django.urls import path
from employee_app.views import *

urlpatterns = [
    path('timesheet/list', timesheet_list, name='timesheet-list'),
    path('timesheet/<int:timesheet_id>/view/', timesheet_view, name='timesheet-view')
]