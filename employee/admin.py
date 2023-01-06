from django.contrib import admin
from .models import Attendanceactions, Attendance

# Register your models here.
admin.site.register(Attendance)
admin.site.register(Attendanceactions)
