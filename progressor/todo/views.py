from django.shortcuts import render

def home(request):

    return render(request,'todo/base.html')