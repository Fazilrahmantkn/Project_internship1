from django.urls import path
from . import views


urlpatterns = [

    path('employees/',
         views.employee_list,
         name='employee_list'),

    path('add-employee/',
         views.add_employee,
         name='add_employee'),

    path('doctors/',
         views.doctor_list,
         name='doctor_list'),

    path('add-doctor/',
         views.add_doctor,
         name='add_doctor'),

    path('companies/',
         views.company_list,
         name='company_list'),

    path('add-company/',
         views.add_company,
         name='add_company'),
]
