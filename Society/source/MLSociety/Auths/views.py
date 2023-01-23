from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Auths.models import Member

# Create your views here.
# giving login authorization
def signin_page(request):
    return render(request, 'loginpage.html')

# creating user 
def signup_page(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        # now confirm the password
        if password1 == password2:
            # data will be pushed in Member and user both tables
            member = Member(name=name, email=email)
            member.save()

            username = email[: len(email)-4]
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # now redirect to login page
            return redirect('/Auth/signin')

        else:
            # show the django message "password didn't matched"
            messages.error(request, "Password didn't match")
            return redirect('/Auth/signup')

    else:
        return render(request, 'signuppage.html')

