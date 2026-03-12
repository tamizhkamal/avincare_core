from django.shortcuts import render

# Create your views here.

def members(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def vision(request):
    return render(request, 'vision.html')

def board(request):
    return render(request, 'board.html')

def quality(request):
    return render(request, 'quality.html')

def products(request):
    return render(request, 'products.html')

def responsibility(request):
    return render(request, 'responsibility.html')

def company(request):
    return render(request, 'company.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def help(request):
    return render(request, 'index.html') 

def logout(request):
    return render(request, 'index.html') 

def login(request):
    return render(request, 'index.html') 

def service(request):
    return render(request, 'service.html') 

def appoinment(request):
    return render(request, 'appoinment.html') 

def team(request):
    return render(request, 'team.html') 

def contact(request):
    return render(request, 'contact.html') 
