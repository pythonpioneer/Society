from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from Auths.models import Member
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
# giving login authorization
def signin_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # now making email as username
        username = email
        user = authenticate(username=username, password=password)

        # now checking for user
        if user is not None:
            # successfully authenticated
            login(request, user)
            # return HttpResponse("Authenticated Successfully!")

            # here, we are adding profile page after login
            # return render(request, "profilepage.html")
            return redirect('/Auth/profile')
        else:
            # failed
            messages.error(request, "Authentication Failed")
            return redirect('/Auth/signin')

    return render(request, 'loginpage.html')

# creating user 
def signup_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        is_registered = False

        # if user direct hits the submit button
        if len(name) == 0 or len(email) == 0 or len(password1) == 0:
            messages.error(request, "Some Fields Are Missing?")
            return redirect('/Auth/signup')

        # now confirm the password
        # error can be thrown by model when same email registerting more than one time--------------------------
        if password1 == password2: 

            # traverse in all users and then check for email/username is unique or not
            users = User.objects.all()

            for usr in users:
                if usr.username == email:
                    is_registered = True

            if is_registered:
                # send the message that email is already in use
                messages.error(request, "Email is Already in Use.")
                return redirect('/Auth/signup')

            else:
                # data will be pushed in Member and user both tables
                member = Member(name=name, email=email)
                member.save()

                user = User.objects.create_user(username=email, email=email, password=password1)
                user.save()            

                # now redirect to login page
                return redirect('/Auth/signin')

        else:
            # show the django message "password didn't matched"
            messages.error(request, "Password didn't match?")
            return redirect('/Auth/signup')

    else:
        return render(request, 'signuppage.html')

# creating a function for logout user
def logout_page(request):
    logout(request)
    return render(request, 'homepage.html')

# profile page, comes after login
@login_required
def profile_page(request):
    return render(request, 'profilepage.html')
    