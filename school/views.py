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

from django.shortcuts import redirect



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
                        context= {'allstudents': yourStudents, 'klasy' : allClasses}  
                        return render(request, 'nauczyciel.html', context)  
                context = {'allstudents': allStudents}
                return render(request, 'admin.html', context)
    context = {}
    return render(request, 'witaj.html', context)
#---------------------------------------------------------
def showAllStudents(request):
    allstudents= Students.objects.all()
    allClasses = Classes.objects.all()
    context= {'allstudents': allstudents, 'klasy' : allClasses}
    return render(request, 'administrator.html', context)

def showClassStudents(request):
    allStudents= Students.objects.all()
    allClasses = Classes.objects.all()
    yourStudents = []
    for student in allStudents:
        if(student.class_field_id== 2):
            yourStudents.append(student)
    context= {'allstudents': yourStudents, 'klasy' : allClasses}
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
    
    context= {'allstudents': nowaKlasaPani, 'klasy' : allClasses}
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
    allClasses = Classes.objects.all()
    context = {'allstudents': allStudents, 'klasy' : allClasses}
    return render(request, 'administrator.html', context)

def edytuj3(request):

    person, created = Employees.objects.update_or_create(employee_id=request.POST['numer'], 
    defaults = {"first_name" : request.POST['your_name'], "middle_name" : request.POST['middle_name'],
     "last_name" : request.POST['last_name'], "salary" : request.POST['salary'], 
    "ptc_comission" : request.POST['ptc_comission'], "phone_number" : request.POST['phone_number'], 
    "email" : request.POST['email'], "hire_date" : request.POST['date'], 
    "manager_id" : request.POST['manager_id'], "job_id" : request.POST['job_id'], 
    "department_id" : request.POST['department_id']})

    adres, created = Addresses.objects.update_or_create(address_id = request.POST['numer_adresu'],
    defaults = {"street_address" : request.POST['street_address'], "postal_code" : request.POST['postal_code'], 
    "city" : request.POST['city'], "country_name" : request.POST['country_name']})
    
    allEmployees = Employees.objects.all()
    allJobs = Jobs.objects.all()
    context = {'allemployees': allEmployees, 'prace' : allJobs}
    return render(request, 'administrator2.html', context)

def admin1(request):
    allStudents = Students.objects.all()
    allClasses = Classes.objects.all()
    context = {'allstudents': allStudents, 'klasy' : allClasses}
    return render(request, 'administrator.html', context)

def admin2(request):
    allEmployees = Employees.objects.all()
    allJobs = Jobs.objects.all()
    context = {'allemployees': allEmployees, 'prace' : allJobs}
    return render(request, 'administrator2.html', context)

def dodaj1(request):
    allEmployees = Employees.objects.all()
    allJobs = Jobs.objects.all()
    allDepartments = Departments.objects.all()

    znalezionyManager = allEmployees
    znalezionaPraca = allJobs
    znalezionyDepartment = allDepartments

    context = {'manager' : znalezionyManager, 'praca': znalezionaPraca, 'departament' : znalezionyDepartment}
    return render(request, 'dodaj1.html', context)

def dodaj2(request):

    context = {}
    return render(request, 'dodaj2.html', context)    

def dodawanieDoBazy(request):
    allEmployees = Employees.objects.all()
    max = 0
    for emp in allEmployees:
        if (emp.employee_id > max):
            max = emp.employee_id



    allAddresses = Addresses.objects.all()
    maxa = 0
    for emp in allAddresses:
        if (emp.address_id > maxa):
            maxa = emp.address_id

    adres, created = Addresses.objects.update_or_create(address_id = (maxa+1),
    defaults = {"street_address" : request.POST['street_address'], "postal_code" : request.POST['postal_code'], 
    "city" : request.POST['city'], "country_name" : request.POST['country_name']})

    person, created = Employees.objects.update_or_create(employee_id=(max+1), 
    defaults = {"first_name" : request.POST['your_name'], "middle_name" : request.POST['middle_name'],
     "last_name" : request.POST['last_name'], "salary" : request.POST['salary'], 
    "ptc_comission" : request.POST['ptc_comission'], "phone_number" : request.POST['phone_number'], 
    "email" : request.POST['email'], "hire_date" : request.POST['date'], 
    "manager_id" : request.POST['manager_id'], "job_id" : request.POST['job_id'], 
    "department_id" : request.POST['department_id'], "address_id" : (maxa+1)})


    
    allEmployees = Employees.objects.all()
    allJobs = Jobs.objects.all()
    context = {'allemployees': allEmployees, 'prace' : allJobs}
    return render(request, 'administrator2.html', context)


def dodawanieUcznia(request):
    allStudents = Students.objects.all()
    max = 0
    for emp in allStudents:
        if (emp.student_id > max):
            max = emp.student_id

    allAddresses = Addresses.objects.all()
    maxa = 0
    for emp in allAddresses:
        if (emp.address_id > maxa):
            maxa = emp.address_id

    allParents = Parents.objects.all()
    maxp = 0 
    for par in allParents:
        if (par.parent_id > maxp):
            maxp = par.parent_id

    klasa = request.POST['class_id']

    allClasses = Classes.objects.all()
    for kl in allClasses:
        if(kl.level == klasa[:1]):
            if(kl.letter == klasa[1:]):
                idklasy = kl.class_id


    adres, created = Addresses.objects.update_or_create(address_id = (maxa+1),
    defaults = {"street_address" : request.POST['street_address'], "postal_code" : request.POST['postal_code'], 
    "city" : request.POST['city'], "country_name" : request.POST['country_name']})

    parent, created = Parents.objects.update_or_create(parent_id=(maxp+1),
    defaults = {
    "first_name" : request.POST['imie_rodzica'],
    "last_name" : request.POST['nazwisko_rodzica'],
    "status" : request.POST['status_rodzica'],
    "phone_number" : request.POST['phone_number_rodzica'],
    "email" : request.POST['email_rodzica']})

    student, created = Students.objects.update_or_create(student_id=(max+1), 
    defaults = {"first_name" : request.POST['your_name'], 
    "middle_name" : request.POST['middle_name'],
    "last_name" : request.POST['last_name'], 
    "gender" : request.POST['gender'], 
    "date_of_birth" : request.POST['date'], 
    "class_field_id" : idklasy, 
    "pesel" : request.POST['pesel'], 
    "parent_id" : (maxp+1), 
    "address_id" : (maxa+1)})

    allStudents = Students.objects.all()
    context = {'allstudents': allStudents, 'klasy' : allClasses}
    return render(request, 'administrator.html', context)    

def usun1(request):
    nr = request.POST['nr_pracownika']

    allEmployees = Employees.objects.all()
    for emp in allEmployees:
        if(emp.employee_id == int(nr)):
            nrad = emp.address_id



    Employees.objects.filter(employee_id = nr).delete()
    Addresses.objects.filter(address_id = nrad).delete()


    allEmployees = Employees.objects.all()
    allJobs = Jobs.objects.all()
    context = {'allemployees': allEmployees, 'prace' : allJobs}
    return render(request, 'administrator2.html', context)

def usun2(request):
    nr = request.POST['nr_studenta']

    allStudents = Students.objects.all()
    for emp in allStudents:
        if(emp.student_id == int(nr)):
            nrad = emp.address_id
            nrrod = emp.parent_id

    allClasses = Classes.objects.all()
   
    
    Parents.objects.filter(parent_id = nrrod).delete()
    Addresses.objects.filter(address_id = nrad).delete()
    Students.objects.filter(student_id = nr).delete()
    
    allEmployees = Students.objects.all()
    context = {'allstudents': allEmployees, 'klasy' : allClasses}
    return render(request, 'administrator.html', context)

