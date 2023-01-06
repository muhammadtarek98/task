from django import forms
from .models import Attendance,Attendanceactions
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields="__all__"
class AttendanceActionForm(forms.ModelForm):
    class Meta:
        model=Attendanceactions
        fields="__all__"