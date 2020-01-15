from django.db import models

# Create your models here.
RELATIONS = (("Father", "Father"),
                    ("Mother", "Mother"),
                    ("Brother", "Brother"),
                    )

SHAPES = (("oval", "oval"),
                 ("rectangular", "rectangular"),
                 ("canopy", "canopy"),
                 ("elevated", "elevated")
                 )
                 

class Relative(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    relation = models.CharField(max_length=50, choices=RELATIONS)
    
    def __str__(self):
        return str(self.name)

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    chapters = models.IntegerField(default=1)
    total_durations = models.IntegerField(default=30)
    
    def __str__(self):
        return str(self.name)

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    doj = models.DateField()
    salary = models.FloatField(default=0)
    subject = models.ManyToManyField("Subject")

    def __str__(self):
        return str(self.name)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    doj = models.DateField()
    standard = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=20)
    ranking = models.CharField(max_length=10, null=True, blank=True)
    poc = models.ManyToManyField("Relative")
    
    def __str__(self):
        return str(self.name)

class Classroom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    seating_capacity = models.IntegerField(default=0)
    web_lec_support = models.BooleanField(default=False)
    shape = models.CharField(max_length=50, choices=SHAPES)
    
    def __str__(self):
        return str(self.name)

class TeacherSubjectClassStudent(models.Model):
    teacher = models.ForeignKey("Teacher", null=True, on_delete=models.SET_NULL)
    class_room = models.ForeignKey("Classroom",  null=True, on_delete=models.SET_NULL)
    subject = models.ManyToManyField("Subject")
    student = models.ManyToManyField("Student")
    
    def __str__(self):
        return str(self.teacher)+" - " +str(self.class_room)