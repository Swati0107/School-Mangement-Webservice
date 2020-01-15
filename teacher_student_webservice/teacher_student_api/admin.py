from django.contrib import admin
from teacher_student_api.models import Teacher, Relative, Student, Classroom, Subject, TeacherSubjectClassStudent
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Relative)
admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(TeacherSubjectClassStudent)
