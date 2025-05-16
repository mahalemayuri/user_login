from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm # type: ignore
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    user = request.user
    template = 'patient_dashboard.html' if user.user_type == 'patient' else 'doctor_dashboard.html'
    return render(request, template, {'user': user})

