"""
from django.shortcuts import render, redirect
from .models import *
from .forms import CourseForm, ModuleForm, LessonForm

def dashboard(request):
    
    return render(request,'instructor/home.html')        


#    coursesForm = Courses.save()
def createCourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('instructor/home.html')
    context = { 'form': form }
    return render(request, 'instructor/courseupload.html',context)

#updating the courses added

def updateCourse(request):

    form = CourseForm(instance=)
    context = {'form': form }
    return render(request, 'instructor/courseupload.html' )

 
    moduleForm = ModuleForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor/home.html')

    lessonForm = LessonForm()
    if request.method == "POST":
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('instructor/home.html')
"""
        


      