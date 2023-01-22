from django.shortcuts import render

# Create your views here.
def signin_page(request):
    return render(request, 'loginpage.html')

def signup_page(request):
    return render(request, 'signuppage.html')
