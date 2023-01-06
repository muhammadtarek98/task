from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('employees_attendance', views.employees_attendance),
    path('employee_checkin_or_checkout', views.employee_checkin_or_checkout),
    path('get_attendance',views.get_attendance)
]
