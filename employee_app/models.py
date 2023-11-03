from django.db import models
from auth_app.models import User

# Create your models here.
    

class Timesheet(models.Model):
    employee = models.ForeignKey(
        User, limit_choices_to={'is_employee': True}, on_delete=models.CASCADE
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField() 
    end_time = models.TimeField()  
    description = models.CharField(max_length=500)

