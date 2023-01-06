# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    day = models.DateField(blank=True, null=True)
    employee = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Attendance'


class Attendanceactions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    attendanceid = models.ForeignKey(Attendance, models.DO_NOTHING, db_column='AttendanceId', blank=True,null=True)  # Field name made lowercase.
    actiontime = models.DateTimeField(db_column='ActionTime', blank=True, null=True)  # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AttendanceActions'
