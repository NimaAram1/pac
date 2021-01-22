from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit , Field

class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        self.fields['username'].help_text = "از نام کاربری مجاز استفاده کنید"
        self.fields['password'].label = "رمز عبور" 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'focus:ring form-md mx-auto text-center'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'focus:ring form-md mx-auto text-center'}))

class UserRegisterationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        self.fields['username'].help_text = "از نام کاربری مجاز استفاده کنید"
        self.fields['password'].label = "رمز عبور"
        self.fields['bio'].label = "درباره خود"
        self.fields['profile_image'].label = "عکس پروفایل"
        self.fields['bio'].required = False
        self.fields['profile_image'].required = False
        self.fields['username'].widget.attrs = {'class':"focus:ring form-md mx-auto text-center"}
        self.fields['password'].widget.attrs = {'class':"focus:ring form-md mx-auto text-center"}
        self.fields['bio'].widget.attrs = {'class':"focus:ring form-md mx-auto text-center"}
        self.fields['profile_image'].widget.attrs = {'class':"focus:ring form-md mx-auto text-center"}

    class Meta:
        model = User
        fields = ['username','password','bio','profile_image'] 
            