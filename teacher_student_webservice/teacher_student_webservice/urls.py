"""teacher_student_webservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from teacher_student_api.views import TeacherSubjectClassStudentController, StudentController, TeacherController, SubjectController, ClassroomController, AllSubjectController, AllTeacherController

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/class_student_teacher_data$', TeacherSubjectClassStudentController().as_view()),
    url(r'^api/teacher_student_data$', StudentController().as_view()),
    url(r'^api/t_data$', TeacherController().as_view()),
    url(r'^api/st_data$', SubjectController().as_view()),

    # Adding data into db
    url(r'^api/teacher_data$', TeacherController().as_view()),
    url(r'^api/student_data$', StudentController().as_view()),
    url(r'^api/subject_data$', SubjectController().as_view()),
    url(r'^api/class_data$', ClassroomController().as_view()),
    url(r'^api/allsubject_data$', AllSubjectController().as_view()),
    url(r'^api/allteacher_data$', AllTeacherController().as_view()),
    
]