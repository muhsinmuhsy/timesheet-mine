from django.shortcuts import render, redirect
from employee_app.models import Timesheet
# Create your views here.


def timesheets(request):
    timesheets = Timesheet.objects.all()

    if request.method == 'POST':
        for timesheet in timesheets:
            status = request.POST.get(f'status_{timesheet.id}')
            if status:
                timesheet.status = status
                timesheet.save()
        return redirect('timesheets')

    context = {'timesheets': timesheets}

    
    return render(request, 'admin/timesheets.html', context)