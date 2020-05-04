from django.conf.urls import url

from . import views

urlpatterns = [
url('witaj',views.witaj),
url('login',views.login),
url('zalogowanie', views.zalogowanie),
url('wezdane1', views.wezdane1),#edycja ucznia przez nauczyciela
url('wezdane2', views.wezdane2),#edycja ucznia przez sekretare
url('wezdane3', views.wezdane3),# edycja pracownika
url('edytuj1', views.edytuj1),#edycja ucznia przez nauczyciela
url('edytuj2', views.edytuj2), #edycja ucznia przez sekretare
url('edytuj3', views.edytuj3), # edycja pracownika
url('admin1', views.admin1), #edycja ucznia
url('admin2', views.admin2), #edycja pracownika
url('dodaj1', views.dodaj1), #dodawanie pracownika
url('dodawanieDoBazy', views.dodawanieDoBazy), #dodawanie pracownika
url('usun1', views.usun1), # usuwanie pracownika
url('dodaj2', views.dodaj2), # dodawanie ucznia
url('dodawanieUcznia', views.dodawanieUcznia), #dodawanie ucznia
url('usun2', views.usun2) # usuwanie ucznia

]
