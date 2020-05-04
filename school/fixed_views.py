# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Students
from .models import Parents
from .models import Classes
from .models import Users
from .models import Addresses
from .models import Employees
from .models import Jobs
from .models import Departments
#
from flask_session import Session
from django.shortcuts import redirect
from flask import Flask, render_template, request,  session, url_for
#dobrze dziala to powyzej 
app = Flask(__name__)
app.secret_key = 'something'

#dobrze dziala!!!! to ponizej
def zalogowanie(request):
    loginOtrzymany = request.POST['login']
    hasloOtrzymane = request.POST['haslo']
    context = {'imie': loginOtrzymany, 'nazwisko' : hasloOtrzymane}
    allUsers = Users.objects.all()
    for user in allUsers:
        if(user.login == loginOtrzymany):
            if (user.password == hasloOtrzymane):
                allStudents= Students.objects.all()
                allClasses= Classes.objects.all()
                yourStudents = []
                for cla in allClasses:
                    if(cla.tutor_id == user.employee_id):
                        for student in allStudents:
                            if(student.class_field_id == cla.class_id):
                                yourStudents.append(student)
                        context= {'allstudents': yourStudents}  
                        return render(request, 'nauczyciel.html', context)  
                context = {'allstudents': allStudents}
                return render(request, 'admin.html', context)
    context = {}
    return render(request, 'witaj.html', context)
#---------------------------------------------------------
def showAllStudents(request):
    allstudents= Students.objects.all()
    context= {'allstudents': allstudents}
    return render(request, 'administrator.html', context)

def showClassStudents(request):
    allStudents= Students.objects.all()
    yourStudents = []
    for student in allStudents:
        if(student.class_field_id== 2):
            yourStudents.append(student)
    context= {'allstudents': yourStudents}
    return render(request, 'nauczyciel.html', context)
#---------------------------------------------------------
def witaj(request):
    context = {}
    return render(request, 'witaj.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

#---------------------------------------------------------
def index(request):
    return HttpResponse("Hello, world!.")

#-----------------------------
def wezdane1(request):
    nrstud = request.POST['nr_studenta']
    allStudents = Students.objects.all()
    allClasses = Classes.objects.all()
    allParents = Parents.objects.all()
    allAddresses = Addresses.objects.all()
    for student in allStudents:
        if(student.student_id == int(nrstud)):
            znalezionyCzlowiek = []
            znalezionyCzlowiek.append(student)
            znalezionyRodzic = []
            znalezionyAdres = []
            for par in allParents:
                if (par.parent_id == student.parent_id):
                    znalezionyRodzic.append(par)
            for adr in allAddresses:
                if (adr.address_id == student.address_id):
                    znalezionyAdres.append(adr)

            context = {'student' : znalezionyCzlowiek, 'klasy' : allClasses, 'rodzic' : znalezionyRodzic, 'adres': znalezionyAdres}
            return render(request, 'edycja.html', context)

def wezdane2(request):
    nrstud = request.POST['nr_studenta']
    allStudents = Students.objects.all()
    allClasses = Classes.objects.all()
    allParents = Parents.objects.all()
    allAddresses = Addresses.objects.all()
    for student in allStudents:
        if(student.student_id == int(nrstud)):
            znalezionyCzlowiek = []
            znalezionyCzlowiek.append(student)
            znalezionyRodzic = []
            znalezionyAdres = []
            for par in allParents:
                if (par.parent_id == student.parent_id):
                    znalezionyRodzic.append(par)
            for adr in allAddresses:
                if (adr.address_id == student.address_id):
                    znalezionyAdres.append(adr)

            context = {'student' : znalezionyCzlowiek, 'klasy' : allClasses, 'rodzic' : znalezionyRodzic, 'adres': znalezionyAdres}
            return render(request, 'edycja2.html', context)

def wezdane3(request):
    nrprac = request.POST['nr_pracownika']
    allEmployees = Employees.objects.all()
    allAddresses = Addresses.objects.all()
    allJobs = Jobs.objects.all()
    allDepartments = Departments.objects.all()
    for emp in allEmployees:
        if(emp.employee_id == int(nrprac)):
            znalezionyCzlowiek = []
            znalezionyCzlowiek.append(emp)
            znalezionyAdres = []
            for adr in allAddresses:
                if (adr.address_id == emp.address_id):
                    znalezionyAdres.append(adr)
            znalezionyManager = allEmployees
            znalezionaPraca = allJobs
            znalezionyDepartment = allDepartments

            context = {'employee' : znalezionyCzlowiek, 'adres' : znalezionyAdres, 
            'manager' : znalezionyManager, 'praca': znalezionaPraca, 'departament' : znalezionyDepartment}
            return render(request, 'edycja3.html', context)


def edytuj1(request):
    numer = request.POST['numer']
    imie = request.POST['your_name']
    drugieimie = request.POST['middle_name']
    nazwisko = request.POST['last_name']
    plec = request.POST['gender']
    data = request.POST['date']
    klasa = request.POST['class_id']
    peselek = request.POST['pesel']

    allClasses = Classes.objects.all()
    for kl in allClasses:
        if(kl.level == klasa[:1]):
            if(kl.letter == klasa[1:]):
                idklasy = kl.class_id

    allStudents = Students.objects.all()
    for stu in allStudents:
        if(stu.student_id == int(numer)):
            staraKlasa = stu.class_field_id

    person, created = Students.objects.update_or_create(student_id=numer, 
    defaults = {"first_name" : imie, "middle_name" : drugieimie, "last_name" : nazwisko, "gender" : plec, 
    "date_of_birth" : data, "class_field_id" : idklasy, "pesel" : peselek})

    adres, created = Addresses.objects.update_or_create(address_id = request.POST['numer_adresu'],
    defaults = {"street_address" : request.POST['street_address'], "postal_code" : request.POST['postal_code'], 
    "city" : request.POST['city'], "country_name" : request.POST['country_name']})

    osoba, created = Parents.objects.update_or_create(parent_id=request.POST['numer_rodzica'],
    defaults = { "first_name" : request.POST['imie_rodzica'], "last_name" : request.POST['nazwisko_rodzica'],
    "status" : request.POST['status_rodzica'], "phone_number" : request.POST['phone_number_rodzica'],
    "email" :  request.POST['email_rodzica']})


    nowaKlasaPani = []
    for stu in allStudents:
        if(stu.class_field_id == staraKlasa):
            nowaKlasaPani.append(stu)
    
    context= {'allstudents': nowaKlasaPani}
    return render(request, 'nauczyciel.html', context)  
    return HttpResponse("Hello, world!." + plec)

def edytuj2(request):
    numer = request.POST['numer']
    imie = request.POST['your_name']
    drugieimie = request.POST['middle_name']
    nazwisko = request.POST['last_name']
    plec = request.POST['gender']
    data = request.POST['date']
    klasa = request.POST['class_id']
    peselek = request.POST['pesel']

    allClasses = Classes.objects.all()
    for kl in allClasses:
        if(kl.level == klasa[:1]):
            if(kl.letter == klasa[1:]):
                idklasy = kl.class_id

    

    person, created = Students.objects.update_or_create(student_id=numer, 
    defaults = {"first_name" : imie, "middle_name" : drugieimie, "last_name" : nazwisko, "gender" : plec, 
    "date_of_birth" : data, "class_field_id" : idklasy, "pesel" : peselek})

    adres, created = Addresses.objects.update_or_create(address_id = request.POST['numer_adresu'],
    defaults = {"street_address" : request.POST['street_address'], "postal_code" : request.POST['postal_code'], 
    "city" : request.POST['city'], "country_name" : request.POST['country_name']})

    osoba, created = Parents.objects.update_or_create(parent_id=request.POST['numer_rodzica'],
    defaults = { "first_name" : request.POST['imie_rodzica'], "last_name" : request.POST['nazwisko_rodzica'],
    "status" : request.POST['status_rodzica'], "phone_number" : request.POST['phone_number_rodzica'],
    "email" :  request.POST['email_rodzica']})
    
    allStudents = Students.objects.all()
    context = {'allstudents': allStudents}
    return render(request, 'administrator.html', context)

def admin1(request):
    allStudents = Students.objects.all()
    context = {'allstudents': allStudents}
    return render(request, 'administrator.html', context)

def admin2(request):
    allEmployees = Employees.objects.all()
    context = {'allemployees': allEmployees}
    return render(request, 'administrator2.html', context)