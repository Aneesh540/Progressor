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

    all_directories = models.Directory.objects.all()
    pwd = models.Directory.objects.get(pk=dir_id)




    new_dir_form = forms.NewDirectoryForm()
    add_todo_form = forms.AddTodoentry()

    context = {
           'pwd': pwd,
           'all_directories': all_directories,
           'new_dir_form':new_dir_form,
           'add_todo_form': add_todo_form}

    if request.method == "POST":

        new_todo = forms.AddTodoentry(request.POST)

        if new_todo.is_valid():
            entry = new_todo.cleaned_data["input_text"]

            directory.todoentry_set.create(entry=entry) # no need to call save


    return render(request,'todo/directory_content.html',context=context)



def view_important(request):
    pass

def testing(request):
    return HttpResponse("testing completed")