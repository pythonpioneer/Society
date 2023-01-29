from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'homepage.html')

def about_page(request):
    return HttpResponse("this is about page")
