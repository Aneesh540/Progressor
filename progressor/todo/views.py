from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from . import models
from . import forms

def home(request):
    new_dir_form = forms.NewDirectoryForm()
    directory = models.Directory.objects.all()
    context = {'directory': directory,'new_dir_form':new_dir_form}

    return render(request,'todo/base.html',context=context)

@require_POST
def add_directory(request):
    new_from = forms.NewDirectoryForm(request.POST)

    if new_from.is_valid():
        new_from.save()

    return redirect('home')





def directory_content(request,dir_id):

    directory = models.Directory.objects.get(pk=dir_id)

    directory_todos = directory.todoentry_set.all()
    directory_base = models.Directory.objects.all()

    new_dir_form = forms.NewDirectoryForm()
    add_todo_entry = forms.AddTodoentry()

    context = {'directory_todos':directory_todos,
           'pwd': directory,
           'directory': directory_base,
           'new_dir_form':new_dir_form,
           'add_todo_entry': add_todo_entry}

    if request.method == "POST":
        print("febwvbwvwbvwvbvbwvb")
        new_todo = forms.AddTodoentry(request.POST)

        if new_todo.is_valid():
            entry = new_todo.cleaned_data["input_text"]

            directory.todoentry_set.create(entry=entry) # no need to call save


    return render(request,'todo/directory_content.html',context=context)