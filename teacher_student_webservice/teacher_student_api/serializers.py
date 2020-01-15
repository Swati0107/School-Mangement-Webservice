from .models import *

from rest_framework import serializers

class TeacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields =("name", "salary")


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields =("name", "doj", "standard", "roll_no", "ranking")


class ClassroomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields =("name", "seating_capacity", "web_lec_support")

class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields =("name", "chapters", "total_durations") 
