from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'homepage.html')

def about_page(request):
    return render(request, 'underconstruction.html')

# adding an underconstruction page
def pythonpioneer_under_construction_page(request):
    return render(request, 'underconstruction.html')
