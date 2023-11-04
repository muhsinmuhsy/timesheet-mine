from django.shortcuts import render, redirect
from employee_app.models import *
from django.contrib import messages
from datetime import datetime, time

# Create your views here.

def timesheet_list(request):
    
    try:
        user = request.user
        timesheets = Timesheet.objects.filter(employee=user)

        for timesheet in timesheets:
            start_time = datetime.combine(datetime.now().date(), timesheet.start_time)
            end_time = datetime.combine(datetime.now().date(), timesheet.end_time)
            duration = end_time - start_time
            total_minutes = int(duration.total_seconds() / 60)
            timesheet.duration = f"{total_minutes:02d}"   
    except:
        messages.error(request, 'not found')
        return redirect('timesheet-list')

    context = {
        'timesheets': timesheets
    }
    return render(request, 'employee/timesheet-list.html', context)



def timesheet_view(request, timesheet_id):
    try:
        timesheet = Timesheet.objects.get(id=timesheet_id)
        start_time = datetime.combine(datetime.now().date(), timesheet.start_time)
        end_time = datetime.combine(datetime.now().date(), timesheet.end_time)
        duration = end_time - start_time
        total_minutes = int(duration.total_seconds() / 60)
        timesheet.duration = f"{total_minutes:02d}"
    except:
        messages.error(request, 'not found')
        return redirect('timesheet-list')
    
    
    context = {
        'timesheet' : timesheet,
        'duration' : duration
    }
    return render(request, 'employee/timesheet-view.html', context)


def timesheet_add(request):
    
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description')

        try:
        
            timesheet = Timesheet(
                employee=request.user,
                status='Pending',
                start_time=start_time,
                end_time=end_time,
                description=description
            )
            timesheet.save()
            messages.success(request, 'add successfully')
            return redirect('timesheet-list')
        except Exception as e:
            messages.error(request, f'faild to add, {str(e)}')
            return redirect('timesheet-add')
        
    return render(request, 'employee/timesheet-add.html')

def timesheet_delete(request, timesheet_id):
    try:
        timesheet = Timesheet.objects.get(id=timesheet_id)
        timesheet.delete()
        messages.success(request, 'deleted successfully')
        return redirect('timesheet-list')
    except:
        messages.error(request, 'deleted faild')
        return redirect('timesheet-list')
    