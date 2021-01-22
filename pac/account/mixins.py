# my mixins
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate , login 
class LoginProtecter:
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect("company:home")
        return super().dispatch(request,*args,**kwargs)    
        

class LoginProtecterElse:
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
             return redirect("company:home")
        return super().dispatch(request,*args,**kwargs)
                
        

