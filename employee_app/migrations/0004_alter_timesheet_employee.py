# Generated by Django 4.2.3 on 2023-11-04 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_app', '0003_alter_timesheet_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='employee',
            field=models.ForeignKey(limit_choices_to={'is_employee': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
