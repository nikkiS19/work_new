"""
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Course(models.Model): 
    title = models.CharField(max_length = 200) 
    description = models.TextField()
    prequestives =  models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
   # img = models.ImageField(upload_to = "instructor/files") 
    #course_id = models.IntegerField()
    last_modified = models.DateTimeField(auto_now_add = True) 

    #membership = 
   
    def __str__(self) : 
        return self.title 

class Module(models.Model):
    title = models.CharField(max_length = 300)
    module_num = models.ForeignKey(Course,on_delete=models.CASCADE)
        #foreign key

    def __str__(self): 
        return self.title 

class Lesson(models.Model):
    #lesson_id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 300) 
    files =  models.FileField(upload_to='instructor/files', null=True, verbose_name="")
    lesson_to_module = models.ForeignKey(Module,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title #+ ": " + str(self.files)   
"""