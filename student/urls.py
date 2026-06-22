from django.urls import path
from . import views
#from .views import 
urlpatterns = [
    path('', views.home, name='home'),

    path('index/', views.index, name='index'),

    path('hello/', views.hello_world, name='hello_world'),

    path('register/', views.studentregister, name='register'),
    path('students/', views.studyview, name='students'),
    path('edit/<int:id>/', views.editdata, name='edit'),
    path('update/<int:id>/', views.dataupdate, name='update'),

    path(
        'apistudent-list/',
        views.StudentListCreateView.as_view()
    ),
    path(
        'apistudent/<int:id>/',
        views.StudentRetrieveUpdateDelete.as_view()
    ),
    path(
        'apiteacher/',
        views.TeacherListCreateView.as_view()
    ),
    path(
        'apiteacher/<int:id>',
        views.TeacherRetrieveUpdateDelete.as_view()
    ),
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

"""
from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Student
    path('studentregister/', views.studentregister, name='studentregister'),

    path('studyview/', views.studyview, name='studyview'),

    path('editdata/<int:id>/',
         views.editdata,
         name='editdata'),

    path('dataupdate/<int:id>/',
         views.dataupdate,
         name='dataupdate'),

    path('deletedata/<int:id>/',
         views.deletedata,
         name='deletedata'),

    # Teacher
    path('teacherregister/',
         views.teacherregister,
         name='teacherregister'),

    path('teacherview/',
         views.teacherview,
         name='teacherview'),

    path('teacheredit/<int:id>/',
         views.teacheredit,
         name='teacheredit'),

    path('teacherupdate/<int:id>/',
         views.teacherupdate,
         name='teacherupdate'),

    path('teacherdelete/<int:id>/',
         views.teacherdelete,
         name='teacherdelete'),
]
"""
