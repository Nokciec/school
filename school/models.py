# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    country_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'addresses'


class Classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    letter = models.CharField(max_length=1, blank=True, null=True)
    tutor = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        db_table = 'classes'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30, blank=True, null=True)
    manager = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        db_table = 'departments'


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ptc_comission = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    hire_date = models.DateField(blank=True, null=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    manager = models.ForeignKey('self', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        db_table = 'employees'


class JobHistory(models.Model):
    job_history_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING)

    class Meta:
        db_table = 'job_history'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=40, blank=True, null=True)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'jobs'


class Parents(models.Model):
    parent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'parents'


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    pesel = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(Parents, models.DO_NOTHING)
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    

    def aaa(self):
	return '%s' % (self.student_id)

    class Meta:
        db_table = 'students'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BinaryField(blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        db_table = 'users'
