from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from auth_app.models import  User
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return render(request, 'auth/login.html')

        if user.check_password(password):
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Login Successfully')
                return redirect('index')
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Incorrect password.')

        return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        email = request.POST.get('email')
        
        
        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')

            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name=first_name, 
                last_name=last_name,
                email=email,
                is_employee = True
                )
            user.save()
            
            # Log the user in after registration
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            messages.success(request, 'Registered Successfully and logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

    return render(request, 'auth/register.html')