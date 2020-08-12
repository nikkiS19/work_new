"""
from django.forms import ModelForm
from .models import Course, Module, Lesson

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'prequestives']

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['title']


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'files']

"""