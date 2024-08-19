from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model 
from account.forms import *
from django.contrib.auth import authenticate, login, logout
from CAFFOOD.models.customer import Customer
from django.contrib import messages
from django.shortcuts import get_object_or_404
from account.utils import EmailSender, send_customer_verify_code, check_user_status


# Create your views here.
User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password1'] 
            customer = Customer.objects.create(user=user, name=user.username, password=password)
            return redirect('verify-customer-email')
        else:
            messages.error(request, 'Registration failed. Please enter correct details.')
    else:
        form = UserRegisterForm()

    return render(request, 'auths/register.html', {'form': form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if not check_user_status(email):
                    return redirect('food')
                return redirect('admin-dashboard')
            else:
                messages.info(request, 'invalid credentials, login fialed!')
        else:
            form = LoginForm()
    return render(request, 'auths/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('food')

def send_email_verify_code(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_customer_verify_code(email)
            messages.success(request, 'a verification code has been sent to your email address')
            return redirect('verify-customer-code')
        else:
            messages.error(request, 'invald code!, enter correct code')
    else:
        form = EmailForm()
    return render(request, 'auths/email.html', {'form': form})

def verify_customer_email_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            users = User.objects.filter(verify_code=code)
            if users.exists():
                for user in users:
                    user.is_verified = True
                    user.save()
                    EmailSender().send_account_registration_mail(user)
                messages.success(request, 'email verification successfully!')
                return redirect('login')
            else:
                messages.error(request, 'invald code!, enter correct code')
        else:
            messages.error(request, 'invald code!, enter correct code')
    else:
        form = CodeForm()
    return render(request, 'auths/code.html', {'form': form})


def send_reset_password_email_verify_code(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_customer_verify_code(email)
            messages.success(request, 'a verification code has been sent to your email address')
            return redirect('password-reset')
        else:
            messages.error(request, 'invald code!, enter correct code')
    else:
        form = EmailForm()
    return render(request, 'auths/email.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            user = get_object_or_404(User, verify_code=code)
            new_password = form.cleaned_data['password']
            user.set_password(new_password)
            user.save()
            EmailSender().send_account_registration_mail(user)
            messages.success(request, 'password reset successful. You can now login with your new password.')
            return redirect('login')
        else:
            messages.error(request, 'password reset failed. Please enter a valid code and password.')
    else:
        form = ResetPasswordForm()
    return render(request, 'auths/reset_password.html', {'form': form})