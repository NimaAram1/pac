from django.shortcuts import render
from django.views.generic import ListView , View

class Home(View):
    def get(self,request):
        return render(request,'home.html')
