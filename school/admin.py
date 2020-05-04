# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Addresses
from .models import Classes
from .models import Departments
from .models import Employees
from .models import JobHistory
from .models import Jobs
from .models import Parents
from .models import Students
from .models import Users
admin.site.register(Addresses)
admin.site.register(Classes)
admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(JobHistory)
admin.site.register(Jobs)
admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Users)
