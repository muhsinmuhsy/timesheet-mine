from django.urls import path
from employee_app.views import *

urlpatterns = [
    path('timesheet/list', timesheet_list, name='timesheet-list'),
    path('timesheet/<int:timesheet_id>/view/', timesheet_view, name='timesheet-view'),
    path('timesheet/add', timesheet_add, name='timesheet-add'),
    path('timesheet/<int:timesheet_id>/delete/', timesheet_delete, name='timesheet-delete'),
]