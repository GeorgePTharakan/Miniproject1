from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def Signup(request):
    if request.method == 'POST':
        

        username = request.POST.get('username')
        email_id = request.POST['email']
        password = request.POST.get('password')
        
        # Validate the credentials or perform any additional checks
        
        # Create a new user profile
        #user_profile = UserProfile.objects.create(username=username, password=password)
        user_profile = UserProfile(username=username,email_id=email_id, password=password)
        user_profile.save()
        
        # Redirect the user to the landing page or any other desired page
       
        return redirect('LandingAfterLogin')
    
    return render(request, 'Signup.html')






def LandingBeforeLogin(request):
    # Handle the landing page logic here
    return render(request, 'LandingBeforeLogin.html')
'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('landingpage'))
        else:
            # Invalid credentials, handle the error or display a message
            
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

            pass
    return render(request, 'login.html')

'''

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_profiles = UserProfile.objects.all()
        for user_profile in user_profiles:
            un = user_profile.username
            pd = user_profile.password

  
            if un == username and pd == password:
                return redirect('LandingAfterLogin')
        
        error_message = 'Invalid username or password.'
        return render(request, 'Login.html', {'error_message': error_message})   
    return render(request, 'Login.html')

def LandingAfterLogin(request):
    return render(request, 'LandingAfterLogin.html')

def Profile(request):
    return render(request, 'Profile.html')

def About(request):
    return render(request, 'About.html')

def Courses(request):
    return render(request, 'Courses.html')

def Cppcourse(request):
    return render(request, 'Cppcourse.html')

def Javacourse(request):
    return render(request, 'Javacourse.html')

def Pythoncourse(request):
    return render(request, 'Pythoncourse.html') 
                    
                

     





