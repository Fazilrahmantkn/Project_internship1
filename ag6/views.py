
from django.shortcuts import render, redirect
from .models import Employee, Doctor, Company


# Employee View
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,
                  'employee_list.html',
                  {'employees': employees})
def add_employee(request):

    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            salary=request.POST['salary']
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')

# Doctor Views
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request,
                  'doctor_list.html',
                  {'doctors': doctors})


def add_doctor(request):

    if request.method == 'POST':
        Doctor.objects.create(
            name=request.POST['name'],
            specialization=request.POST['specialization'],
            experience=request.POST['experience']
        )
        return redirect('doctor_list')

    return render(request, 'add_doctor.html')


# Company Views
def company_list(request):
    companies = Company.objects.all()
    return render(request,
                  'company_list.html',
                  {'companies': companies})


def add_company(request):

    if request.method == 'POST':
        Company.objects.create(
            name=request.POST['name'],
            location=request.POST['location'],
            employees=request.POST['employees']
        )
        return redirect('company_list')

    return render(request, 'add_company.html')
# Create your views here.
