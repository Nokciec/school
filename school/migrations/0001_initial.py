# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-05 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('country_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(blank=True, max_length=1, null=True)),
                ('letter', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ptc_comission', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Addresses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Departments')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('job_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Employees')),
            ],
            options={
                'db_table': 'job_history',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(blank=True, max_length=40, null=True)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'parents',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('pesel', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Addresses')),
                ('class_field', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.DO_NOTHING, to='school.Classes')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Parents')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.AddField(
            model_name='jobhistory',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Jobs'),
        ),
        migrations.AddField(
            model_name='employees',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Jobs'),
        ),
        migrations.AddField(
            model_name='employees',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Employees'),
        ),
        migrations.AddField(
            model_name='departments',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Employees'),
        ),
        migrations.AddField(
            model_name='classes',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Employees'),
        ),
    ]
