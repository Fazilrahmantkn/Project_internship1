from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Student, Teacher
from django.http import HttpResponse


def new(request):
    p = 'python language'
    k = [10, 20, 30, 5, 50]
    l = 100
    return render(request, 'student/one.html', {'p1': p, 'k1': k, 'l1': l})
    return HttpResponse("Hello World")


# ---------------- STUDENT ----------------
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Teacher

# ========== STUDENT VIEWS ==========
"""
# ➤ Register student
def student_register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        Student.objects.create(name=fname, age=age, email=email)
        return HttpResponse("Student registration successful")
    return render(request, "student.html")

# ➤ View all students
def student_list(request):
    students = Student.objects.all()
    return render(request, "studentview.html", {"sview": students})

# ➤ Delete student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect(student_list)

# ========== TEACHER VIEWS ==========

# ➤ Register teacher
def teacher_register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Teacher.objects.create(name=fname, age=age, email=email, subject=subject)
        return HttpResponse("Teacher registration successful")
    return render(request, "teacher.html")

# ➤ View all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacherview.html", {"tview": teachers})

# ➤ Delete teacher
def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect(teacher_list)

"""
def home(request):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()

    context = {
        'student_count': student_count,
        'teacher_count': teacher_count,
    }

    return render(request, 'home.html', context)
from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Studymodel, Student, Teacher


def index(request):
    return redirect('/admin/')


def hello_world(request):
    return HttpResponse("Hello World")


# FUNCTION BASED CRUD

def studentregister(request):

    if request.method == 'POST':
        Studymodel.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email']
        )
        return redirect('students')

    return render(request, 'studentform.html')


def studyview(request):
    students = Studymodel.objects.all()
    return render(
        request,
        'studentlist.html',
        {'students': students}
    )


def editdata(request, id):
    student = get_object_or_404(
        Studymodel,
        id=id
    )

    return render(
        request,
        'dataedit.html',
        {'student': student}
    )


def dataupdate(request, id):

    student = get_object_or_404(
        Studymodel,
        id=id
    )

    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.save()

        return redirect('students')

    return render(
        request,
        'dataedit.html',
        {'student': student}
    )


# STUDENT CBV

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')


# TEACHER CBV

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_delete.html'
    success_url = reverse_lazy('teacher_list')
