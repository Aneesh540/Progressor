from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from . import models
from . import forms



def view_important(request):
    all_directories = models.Directory.objects.all()
    all_todos = models.Todoentry.objects.all()
    new_dir_form = forms.NewDirectoryForm()
    total_important_items = models.Todoentry.objects.filter(important=True,completed=False).count()

    context = {'all_directories':all_directories,
               'new_dir_form':new_dir_form,
               'all_todos':all_todos,
               'total_important_items':total_important_items}

    return render(request,'todo/important.html',context=context)

@require_POST
def add_directory(request):
    new_from = forms.NewDirectoryForm(request.POST)

    if new_from.is_valid():
        new_folder = new_from.save()

    return redirect(new_folder)


def directory_content(request,dir_id):

    all_directories = models.Directory.objects.all()
    pwd = models.Directory.objects.get(pk=dir_id)
    total_important_items = models.Todoentry.objects.filter(important=True).count()

    todo_list = pwd.todoentry_set.order_by('completed')

    new_dir_form = forms.NewDirectoryForm()
    add_todo_form = forms.AddTodoentry()

    context = {
           'pwd': pwd,
           'all_directories': all_directories,
            'todo_list':todo_list,
           'new_dir_form':new_dir_form,
           'add_todo_form': add_todo_form,
            'total_important_items':total_important_items}

    if request.method == "POST":

        new_todo = forms.AddTodoentry(request.POST)

        if new_todo.is_valid():
            entry = new_todo.cleaned_data["input_text"]

            pwd.todoentry_set.create(entry=entry) # no need to call save


    return render(request,'todo/directory_content.html',context=context)


def delete_folder(request,dir_id):
    folder = models.Directory.objects.get(pk=dir_id)
    folder.delete()

    return redirect('important')


def delete_completed(request,dir_id):
    folder = models.Directory.objects.get(pk=dir_id)

    todo_to_delete = folder.todoentry_set.filter(completed__exact=True)
    todo_to_delete.delete()

    return redirect(folder)


def delete_all(request,dir_id):
    folder = models.Directory.objects.get(pk=dir_id)
    todo_to_delete = folder.todoentry_set.all()
    todo_to_delete.delete()

    return redirect(folder)


def aliter_status(request,todo_id):
    todo_instance = models.Todoentry.objects.get(pk=todo_id)
    todo_instance.completed = not todo_instance.completed
    todo_instance.save()

    return redirect(todo_instance.basedir)


def change_importance(request,todo_id):
    todo_instance = models.Todoentry.objects.get(pk=todo_id)
    todo_instance.important = not todo_instance.important
    todo_instance.save()

    return redirect(todo_instance.basedir)


def for_important(request,todo_id,dir_id=1):

    todo_instance = models.Todoentry.objects.get(pk=todo_id)
    todo_instance.completed = not todo_instance.completed
    todo_instance.save()

    return redirect('important')
