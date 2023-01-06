# from .models import Attendanceactions, Attendance
from datetime import datetime, date, timedelta
import sqlite3


def get_attendance(employee_name: str, date: date):
    connection = sqlite3.Connection(r'E:\PythonTask\PythonTask\task\task\attendance.db')
    cursor = connection.cursor()
    full_query = f"""
select Attendance.Id,AttendanceActions.AttendanceId,Attendance.employee,AttendanceActions.Action,AttendanceActions.ActionTime 
from Attendance JOIN AttendanceActions 
on(Attendance.employee='{employee_name}' AND Attendance.Id==AttendanceActions.AttendanceId AND AttendanceActions.ActionTime like '{date}%')
"""
    cursor.execute(full_query)
    employee_query_output = cursor.fetchall()
    # cursor.execute(date_attendance_query)
    date_attendance_output = cursor.fetchall()
    checkin = list()
    checkout = list()
    for row in employee_query_output:
        if row[3] == 'CheckIn':
            checkin = row
        elif row[3] == 'CheckOut':
            checkout = row
    checkindate = checkin[-1]
    checkoutdate = checkout[-1]
    format = '%Y-%m-%d %I:%M %p'
    checkindate = datetime.strptime(checkindate, format)
    checkoutdate = datetime.strptime(checkoutdate, format)
    attended = False
    if checkoutdate - checkindate:
        attended = True
    diff = abs(checkoutdate - checkindate)
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    duration = f'{hours}:{minutes}:{seconds}'
    return {'attended': attended, 'duration': duration}
    connection.commit()
    connection.close()


test1 = get_attendance(employee_name='EMP01', date='2020-04-01')
test2= get_attendance(date='2020-04-02',employee_name='EMP01')
print(test1)
print(test2)
