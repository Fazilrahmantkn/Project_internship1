from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('hello/', views.hello_world, name='hello_world'),

    path('register/', views.studentregister, name='register'),
    path('students/', views.studyview, name='students'),
    path('edit/<int:id>/', views.editdata, name='edit'),
    path('update/<int:id>/', views.dataupdate, name='update'),

    path(
        'student-list/',
        views.StudentListView.as_view(),
        name='student_list'
    ),

    path(
        'student-add/',
        views.StudentCreateView.as_view(),
        name='student_add'
    ),

    path(
        'student-update/<int:pk>/',
        views.StudentUpdateView.as_view(),
        name='student_update'
    ),

    path(
        'student-delete/<int:pk>/',
        views.StudentDeleteView.as_view(),
        name='student_delete'
    ),

    path(
        'teacher-list/',
        views.TeacherListView.as_view(),
        name='teacher_list'
    ),

    path(
        'teacher-add/',
        views.TeacherCreateView.as_view(),
        name='teacher_add'
    ),

    path(
        'teacher-update/<int:pk>/',
        views.TeacherUpdateView.as_view(),
        name='teacher_update'
    ),

    path(
        'teacher-delete/<int:pk>/',
        views.TeacherDeleteView.as_view(),
        name='teacher_delete'
    ),
]
