from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    count=User.objects.count()
    return render (request, 'home.html', {
        'count':count
    })

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            send_email(
                'Confirmation Mail',
                'congratulations, You are successfully registered .',
                settings.EMAIL_HOST_USER,
                ['to@example.com'],
                fail_silently=False
            )
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form':form
    })