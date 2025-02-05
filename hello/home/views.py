
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from home.models import Contact 
from django.contrib import messages
from django.shortcuts import render, redirect

 # Corrected the import

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact_view(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact_reason = request.POST.get('contact_reason')  # Get the contact reason
       
        message = request.POST.get('message')
        if contact_reason is None:
            contact_reason = '1'  
       
    
        if fullname and email and message:  # Validate fields
            new_contact = Contact(
                fullname=fullname, 
                email=email, 
                phone=phone, 
                contact_reason=contact_reason, 
                message=message, 
                date=datetime.today()
            )
            new_contact.save()
            messages.success(request, "Your message has been successfully sent!")
        else:
            messages.error(request, "Please fill out all required fields.")
            return redirect('contact')  # Redirect to contact page or success page
    return render(request, 'contact.html')
def login_view(request):
    login_failed = False  # Define the variable before the if statements
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to homepage or dashboard
        else:
            login_failed = True  # Set this flag when login fails
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html', {'login_failed': login_failed})
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')
def logout_view(request):
    logout(request)
    return redirect('login')


