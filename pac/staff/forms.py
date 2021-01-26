from django import forms
from .models import Staff

class StaffRegisterationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StaffRegisterationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "نام "
        self.fields['last_name'].label = "نام خانوادگی"
        self.fields['job'].label = "سمت" 
        self.fields['resume'].label = "رزومه" 
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['job'].required = True
        self.fields['resume'].required = True 
        self.fields['first_name'].widget.attrs = {"class":"focus:ring form-md mx-auto text-center"}
        self.fields['last_name'].widget.attrs = {"class":"focus:ring form-md mx-auto text-center"}
        self.fields['job'].widget.attrs = {"class":"focus:ring form-md mx-auto text-center"}
        self.fields['resume'].widget.attrs = {"class":"focus:ring form-md mx-auto text-center"}
    class Meta:
        model = Staff
        fields = ['first_name','last_name','job','resume']