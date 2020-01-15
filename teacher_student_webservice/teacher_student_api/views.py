from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.template import loader

from .models import Teacher, Relative, Student, Classroom, Subject, TeacherSubjectClassStudent
from django.db.models import Sum, Count
from .serializers import TeacherSerializers, SubjectSerializers, ClassroomSerializers, StudentSerializers

class TeacherSubjectClassStudentController(APIView):

    def get(self, request):
        complete_data = TeacherSubjectClassStudent.objects.all().values("teacher__name","class_room__name", "subject__name")
        template = loader.get_template('complete_data.html')

        context = {
        'data': list(complete_data),
        }
        
        return HttpResponse(template.render(context, request))

class TeacherController(APIView):
    
    def post(self, request):
        request_validator = TeacherSerializers(data = request.data)

        if request_validator.is_valid():
            name=request.data['name']
            doj=request.data["doj"]
            salary=request.data["salary"]

            obj, status=Teacher.objects.get_or_create(name=name, doj=doj, salary=salary)

            if status:
                return Response("Teacher data successfully created")
        else:
            return Response("Invalid Request. Please provide valid parameters!")
    def get(self, request):
        teachers_data = TeacherSubjectClassStudent.objects.filter(teacher__salary__gte=int(request.GET['salary'])).annotate(salary_sum=Sum('teacher__salary'))
        final_list =[]

        for data in teachers_data:
            final_dict={}
            final_dict['teacher']= data.teacher.name
            student_count = data.student.all().count()
            final_dict['total_student']= student_count
            final_dict['total_salary']=data.salary_sum
            final_list.append(final_dict)
          
        template = loader.get_template('teacher_data.html')

        context = {
        'data': final_list,
        }
        
        return HttpResponse(template.render(context, request))

class StudentController(APIView):
    
    def post(self, request):
        request_validator = StudentSerializers(data = request.data)
        if request_validator.is_valid():
            name=request.data['name']
            doj=request.data["doj"]
            standard=request.data["standard"]
            roll_no=request.data["roll_no"]
            ranking=request.data["ranking"]
            relative_name=request.data["relative_name"]
            relative_number=request.data["relative_number"]
            relative_relation=request.data["relative_relation"]

            rel, st= Relative.objects.get_or_create(name=relative_name, number=relative_number, relation=relative_relation)
            obj, status=Student.objects.get_or_create(name=name, doj=doj, standard=standard, roll_no=roll_no, ranking=ranking)

            if status:
                return Response("Student data successfully created")
        else:
            return Response("Invalid Request. Please provide valid parameters!")

    def get(self, request):
        if request.GET.get('teacher'):
            student_data = TeacherSubjectClassStudent.objects.filter(teacher__name=request.GET['teacher']).values("teacher__name","student__name")

            template = loader.get_template('student_data.html')

            context = {
            'data': student_data,
            }
            
            return HttpResponse(template.render(context, request))
        else:
            return Response("Invalid Request. Please provide valid parameters!")

class SubjectController(APIView):
    
    def post(self, request):
        request_validator = SubjectSerializers(data = request.data)
        if request_validator.is_valid():
            name=request.data['name']
            chapters=request.data["chapters"]
            total_durations=request.data["total_durations"]

            obj, status=Subject.objects.get_or_create(name=name, chapters=chapters, total_durations=total_durations)

            if status:
                return Response("Subject data successfully created")
        else:
            return Response("Invalid Request. Please provide valid parameters!")

    def get(self, request):
        subject_data = TeacherSubjectClassStudent.objects.values('teacher__name', 'student__name', 'subject__name', 'subject__total_durations').aggregate(studcount=Count('student__name'), timecount=Sum('subject__total_durations'), subcount=Count('teacher__subject'))
        print(subject_data,'---')
        template = loader.get_template('subject_data.html')

        context = {
        'data': subject_data,
        }
        
        return HttpResponse(template.render(context, request))

class ClassroomController(APIView):
    
    def post(self, request):
        request_validator = ClassroomSerializers(data = request.data)

        if request_validator.is_valid():
            name=request.data['name']
            seating_capacity=request.data["seating_capacity"]
            web_lec_support=request.data["web_lec_support"]
            shape=request.data["shape"]

            obj, status=Classroom.objects.get_or_create(name=name, seating_capacity=seating_capacity, web_lec_support=web_lec_support, shape=shape)

            if status:
                return Response("Classroom data successfully created")
        else:
            return Response("Invalid Request. Please provide valid parameters!")

    def get(self, request):
        class_data=Classroom.objects.all().values("name", "seating_capacity", "web_lec_support", "shape")

        template = loader.get_template('classroom_data.html')
        context = {
        'data': class_data,
        }
        
        return HttpResponse(template.render(context, request))


class AllSubjectController(APIView):

    def get(self, request):
        sub_data=Subject.objects.all().values("name", "chapters", "total_durations")

        template = loader.get_template('allsubject_data.html')

        context = {
        'data': sub_data,
        }
        
        return HttpResponse(template.render(context, request))


class AllTeacherController(APIView):

    def get(self, request):
        teac_data=Teacher.objects.all().values("name", "doj", "salary", "subject")

        template = loader.get_template('allteacher_data.html')

        context = {
        'data': teac_data,
        }
        
        return HttpResponse(template.render(context, request))