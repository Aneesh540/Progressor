from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('add_directory/',views.add_directory,name="add_directory"),
    path('directory/<int:dir_id>',views.directory_content,name="directory_content"),
    path('important/',views.view_important,name="important"),
    path('testing',views.testing,name="testing"),

]