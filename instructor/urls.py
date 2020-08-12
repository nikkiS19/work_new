"""
from django.urls import path
from . import views

app_name="instructor"

urlpatterns=[
    path('',views.dashboard,name="home"),
    path('courseupload/',views.createCourse,name="createcourse"),
   # path('updatecourse/',views.updateCourse,name="updatecourse")


]
"""