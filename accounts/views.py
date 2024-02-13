from django.shortcuts import render,redirect
from .forms import RegisterUserForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,  logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import JsonResponse



@login_required(login_url="accounts:user-login")
def home(request):
    upcoming_events = request.user.myEvents.filter(status='upcoming').count()
    return render(request, "main/home.html" , locals())



@login_required(login_url="accounts:user-login")
def profile(request):
    return render(request, "accounts/profile.html")



@login_required(login_url="accounts:user-login")
def update_profile(request):
    obj = CustomUser.objects.get(email = request.user.email )
    
    if request.POST:
        form = UserUpdateForm(request.POST ,instance = obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect("accounts:profile")
        else:
            return render(request, "accounts/update-profile.html" , {'form':form})
    
    form = UserUpdateForm(instance = obj)
    return render(request, "accounts/update-profile.html" , {'form':form})


def user_login(request):    
    if request.POST:
        email = request.POST.get('email')
        raw_password = request.POST.get('password')

        user = authenticate(email=email, password=raw_password)
        if user is not None:
            login(request, user) 
            messages.success(request, "You are logged successfully.")
            return redirect("accounts:home")
        else:
            messages.error(request , "Credentials are not matched")
            return redirect("accounts:user-login")
        
    return render(request , "accounts/login.html")


def user_registration(request):
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate user after registration and redirect to home
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            
            if user is not None:
                login(request, user) 
            else:    
                messages.error(request , "Something Went Wrong! Contact Admin")
                return redirect("accounts:user-register")
            
            messages.success(request, "You are registered successfully.")
            return redirect("accounts:home")
            
        else:
            return render(request , "accounts/register.html" , {'form':form} )    
        
    context={'form': RegisterUserForm() }
    return render(request , "accounts/register.html" , context)


def user_logout(request):
    logout(request)
    messages.success(request , "You are Logout Successfully!")
    return redirect("accounts:user-login")




##########  Forget Password (Workign On It) #####################################
def sent_otp_api(request):
    getEmail = request.GET.get("email")
    if CustomUser.objects.filter(email=getEmail).exists():
        request.session['email'] = getEmail
        request.session['otp'] = 1234 
        CustomUser.objects.filter(email=getEmail).update(
            otp = 1234
        )
        return JsonResponse({'status': "success"})
    else:
        return JsonResponse({'status': "no active account found"})


def forget_pass_view(request):
    
    getEmail = request.GET.get("email")
    getOtp = request.GET.get("otp")
        
    if CustomUser.objects.filter(email=getEmail , otp = getOtp).exists():
        messages.success(request , "OTP Matched SuccessFully")
        return redirect("accounts:set-password")
    


from django.contrib.auth.forms import PasswordResetForm
def set_password_view(request):
    if request.POST:
        form = PasswordResetForm(request.POST)


    form = PasswordResetForm()    
    return render(request , "accounts/set-password.html" ,{'form':form})
