from django.shortcuts import render
from .models import Attendance, Attendanceactions
from datetime import datetime, date, time
from time import time

from django.http import HttpRequest, HttpResponse


# Create your views here.
def main_view(request):
    return render(request=request,
                  template_name=r'E:\PythonTask\PythonTask\task\task\templates\main.html')


def employees_attendance(request):
    attendance = Attendance.objects.all()
    attendance_action = Attendanceactions.objects.all()
    context = {'attendance': attendance, 'attendance_action': attendance_action}
    return render(request=request,
                  template_name=r'E:\PythonTask\PythonTask\task\task\templates\employees attendance.html',
                  context=context)


def employee_checkin_or_checkout(request):
    if request.method == 'POST':
        current_date = datetime.today().strftime('%YYYY-%MM-%DD ')
        current_time = datetime.now().strftime('%I:%M %p')
        if request.POST.post('checkin') == 'checkin':
            employee_name = request.POST['name']
            employees_query = Attendance.objects.raw('select name form Attendance')
            action = Attendanceactions()
            attendance = Attendance()
            if employee_name in employees_query:
                action.action = 'CheckIn'
                action.attendanceid.name = attendance.employee = employee_name
                attendance.day = current_date
                action.actiontime = current_time
                attendance.save()
                action.save()
        if request.POST.post('checkout') == 'checkout':
            employee_name = request.POST['name']
            employees_query = Attendance.objects.raw('select name form Attendance')
            action = Attendanceactions()
            attendance = Attendance()
            if employee_name in employees_query:
                action.action = 'CheckOut'
                action.attendanceid.name = attendance.employee = employee_name
                attendance.day = current_date
                action.actiontime = current_time
                attendance.save()
                action.save()
        return render(request=request,
                      template_name=r'E:\PythonTask\PythonTask\task\task\templates\Employee Checkin.html')


def get_attendance(request):
    employee_name='EMP01'
    employee_name_query = f"""select Id,employee from Attendance where employee='{employee_name}'"""
    date_attendance_query=f""
    attendance_query = Attendance.objects.raw(employee_name_query)
    return render(request=request,
                  template_name=r'E:\PythonTask\PythonTask\task\task\templates\test.html',
                  context={'attendance_query':attendance_query})
