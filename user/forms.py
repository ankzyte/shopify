from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class CreateProfileForm(forms.ModelForm):
    locality = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pincode = forms.CharField()
    class Meta:
        model=Profile
        fields=['locality','city','state','pincode']
