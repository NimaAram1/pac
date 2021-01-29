from django.shortcuts import render ,HttpResponse , redirect ,get_object_or_404
from django.views.generic import View , ListView , DetailView
from staff.models import Staff
from account.models import User
from .forms import StaffRegisterationForm
from django.contrib import messages
from .mixins import StaffProtect

class panel(View):
    def get(self,request):
        if Staff.objects.filter(user=request.user.pk):
            if Staff.objects.filter(user=request.user.pk,setup_completed=False):
                return redirect("staff:setup")
            else:
                return redirect("staff:home")                
        else:
            return redirect("company:home")    


# setupping staff model for user
class setup(StaffProtect,View):
    def get(self,request):
        staff = get_object_or_404(Staff,user=request.user.pk)
        form = StaffRegisterationForm(instance=staff)
        Staff.objects.filter(user=request.user.pk).update(bio=User.objects.filter(pk=request.user.pk).values_list('bio'),profile_image=User.objects.filter(pk=request.user.pk).values_list('profile_image'))
        return render(request,'setup.html',{"form":form})
    def post(self,request):
        staff = get_object_or_404(Staff,user=request.user.pk)
        form = StaffRegisterationForm(request.POST,request.FILES,instance=staff)
        if form.is_valid():
            staff2 = form.save(commit=False)
            staff2.setup_completed = True
            staff2.save()
            messages.success(request,'You created your staff sucessfully.')
            return redirect("company:home") 


# Personal control menu
class home(View):
    def get(self,request):
        staff = get_object_or_404(Staff,user=request.user.pk)
        return render(request,'home_staff.html',{"staff":staff})      


# Public profile
