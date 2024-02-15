from django.shortcuts import render,redirect
from .forms import UserRegisterForm, CreateProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html',context)

@login_required
def profile(request):
    user_profiles = Profile.objects.filter(user=request.user)
    if request.method=="POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,"Address successfully added")
            return redirect('user-address')
    else:
        form = CreateProfileForm()
    context={
        'form':form,
        'user_profiles':user_profiles
    }
    return render(request,"user/profile.html",context)

@login_required
def address(request):
    context={
        'addresses':Profile.objects.filter(user = request.user),
    }
    return render(request,'user/address.html',context)

def user_exists(username):
    try:
        user = User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False

def sendEmail(request):
    if request.method=="POST":
        username = request.POST['username']
        if user_exists(username):
            sendPasswordResetLink(User.objects.get(username=username))
            messages.success(request,'Password Reset link has been sent to your gmail')
            return redirect('user-login')
    return render(request, 'user/send_email.html')

def sendPasswordResetLink(user):
    token = default_token_generator.make_token(user)
    reset_link = f"http://127.0.0.1:8000/resetpassword/{user.id}/{token}"
    subject = "Password Reset"
    message = render_to_string('user/reset_password_email.html', {'reset_link': reset_link})
    send_mail(subject, message, 'shivamcook@gmail.com', [user.email])

def passwordReset(request, user_id, token):
    user = User.objects.get(id=user_id)
    if default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Validate and update password
            new_password = request.POST['new_password']
            user.set_password(new_password)
            user.save()
            messages.success(request,'Password has been reset successfully!')
            return redirect('user-login')
        return render(request, 'user/reset_password.html')
    else:
        return redirect('shop-home')

def changePassword(request):
    if request.method=="POST":
        old_password = request.POST['old_password']
        if request.user.check_password(old_password):
            new_password=request.POST['new_password']
            request.user.set_password(new_password)
            request.user.save()
            return redirect('shop-home')
        else:
            return render(request,'user/change_password.html')
    return render(request,'user/change_password.html')