from django.shortcuts import render ,HttpResponse , redirect ,get_object_or_404
from django.views.generic import View , ListView , DetailView , CreateView
from staff.models import Staff
from account.models import User
from .forms import StaffRegisterationForm , CompanyRegisterationForm
from django.contrib import messages
from .mixins import StaffProtect
from django.utils.text import slugify
from account.models import User
from company.models import Company
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


# creating company

class create_company(CreateView):
    template_name = 'create_company.html'
    form_class = CompanyRegisterationForm
    def form_valid(self,form):
        if Company.objects.filter(founder=self.request.user.pk):
            messages.error(self.request,"You can't create more than 1 company.")
            return redirect("staff:create_company")
        else:    
            company = form.save(commit=False)
            company.slug = slugify(form.cleaned_data.get('name'),allow_unicode=True)
            company.founder = self.request.user
            company.save() 
            messages.success(self.request,'You created your company successfully.')
            return redirect("staff:panel")