# from django.urls import path
# from .views import *
from django.urls import path
from .views import *

# urlpatterns=[
#     path("new",new),
# ]
urlpatterns = [

    # Student URLs
    


    path('', home, name='home'),

    path(
        "students/",
        StudentListView.as_view(),
        name="student_list"
    ),

    path(
        "teachers/",
        TeacherListView.as_view(),
        name="teacher_list"
    ),

    path(
        "students/",
        StudentListView.as_view(),
        name="student_list"
    ),

    path(
        "students/add/",
        StudentCreateView.as_view(),
        name="student_add"
    ),

    path(
        "students/edit/<int:pk>/",
        StudentUpdateView.as_view(),
        name="student_edit"
    ),

    path(
        "students/delete/<int:pk>/",
        StudentDeleteView.as_view(),
        name="student_delete"
    ),

    # Teacher URLs
    path(
        "teachers/",
        TeacherListView.as_view(),
        name="teacher_list"
    ),

    path(
        "teachers/add/",
        TeacherCreateView.as_view(),
        name="teacher_add"
    ),

    path(
        "teachers/edit/<int:pk>/",
        TeacherUpdateView.as_view(),
        name="teacher_edit"
    ),

    path(
        "teachers/delete/<int:pk>/",
        TeacherDeleteView.as_view(),
        name="teacher_delete"
    ),
]