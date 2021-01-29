# my mixins 
from .models import Staff
from django.shortcuts import redirect
class StaffProtect:
    def dispatch(self,request,*args,**kwargs):
        if Staff.objects.filter(user=request.user.pk,setup_completed=True):
            return redirect("company:home")
        return super().dispatch(request,*args,**kwargs)