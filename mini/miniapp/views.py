from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import *

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Validate the credentials or perform any additional checks
        
        # Create a new user profile
        #user_profile = UserProfile.objects.create(username=username, password=password)
        user_profile = UserProfile(username=username, password=password)
        user_profile.save()
        
        # Redirect the user to the landing page or any other desired page
        return redirect('landingpage')
    
    return render(request, 'signin.html')






def landing_page_view(request):
    # Handle the landing page logic here
    return render(request, 'landingpage.html')
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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_profiles = UserProfile.objects.all()
        for user_profile in user_profiles:
            un = user_profile.username
            pd = user_profile.password

  
            if un == username and pd == password:
                return redirect('landingpage')
        
        error_message = 'Invalid username or password.'
        return render(request, 'login.html', {'error_message': error_message})   
    return render(request, 'login.html')
            
                    
                

     





