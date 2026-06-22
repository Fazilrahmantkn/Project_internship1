from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Student, Teacher


# ---------------- STUDENT ----------------

class StudentListView(ListView):
    model = Student
    template_name = "Student_App/student_list.html"
    context_object_name = "students"


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = "Student_App/student_form.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = "Student_App/student_form.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "Student_App/student_delete.html"
    success_url = reverse_lazy("student_list")


# ---------------- TEACHER ----------------

class TeacherListView(ListView):
    model = Teacher
    template_name = "Student_App/teacher_list.html"
    context_object_name = "teachers"


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    template_name = "Student_App/teacher_form.html"
    success_url = reverse_lazy("teacher_list")


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    template_name = "Student_App/teacher_form.html"
    success_url = reverse_lazy("teacher_list")


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "Student_App/teacher_delete.html"
    success_url = reverse_lazy("teacher_list")




def home(request):
    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
    }
    return render(request, "home.html", context)


# # def view_students(self):
# #     model = Student

# from django.shortcuts import render
# def new(request):
#     p = 'python language'
#     k = [10, 20, 30, 5, 50]
#     l = 100
#     return render(request, 'one.html', {'p1':p,'k1':k,'l1':l})

# views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .models import StudyModel


# crud operation - create, read, update, delete

# ➤ Create student (without using forms.py)
def study(request):
    if request.method == "POST":
        fname = request.POST['name']
        age = request.POST['age']
        email = request.POST['emailid']
        Student.objects.create(name=fname,age=age,email=email)
        return HttpResponse("Registration successful")
    return render(request, "study.html")


# ➤ View all students
# def studyview(request):
#     students = Studymodel.objects.all()
#     return render(request, "studyview.html", {"sview": students})


# ➤ Delete student
# def datadelete(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect(studyview)


# # ➤ Load student data for editing
# display the data saved in form format - we can make changes - click update
# def editdata(request, id):
#     student = get_object_or_404(Studymodel, id=id)
#     return render(request, "dataedit.html", {"edit": student})


# # ➤ Update student record
# def dataupdate(request, id):
#     student = get_object_or_404(Studymodel, id=id)
#     if request.method == "POST":
#         student.name = request.POST['name']
#         student.age = request.POST['age']
#         student.email = request.POST['email']
#         student.save()
# data get updated and saved inside the original database
#         return redirect(studyview)
#     return render(request, "dataedit.html", {"edit": student})


# 
