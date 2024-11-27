from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')

def contacts(request):
    return render(request,'contacts.html')

def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')