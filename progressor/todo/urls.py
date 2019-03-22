from django.urls import path
from . import views

urlpatterns = [

    path('',views.view_important,name="home"),
    path('add_directory/',views.add_directory,name="add_directory"),
    path('directory/<int:dir_id>',views.directory_content,name="directory_content"),
    path('important/',views.view_important,name="important"),

    path('delete_folder/<int:dir_id>',views.delete_folder,name="delete_folder"),
    path('delete_completed/<int:dir_id>',views.delete_completed,name="delete_completed"),
    path('delete_all/<int:dir_id>', views.delete_all, name="delete_all"),

    path('aliter_status/<int:todo_id>',views.aliter_status,name="aliter_status"),
    path('aliter_importance/<int:todo_id>',views.change_importance,name="aliter_importance"),

    path('testing/<int:todo_id>',views.for_important,name="for_important"),

]