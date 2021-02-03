from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('panel',views.panel.as_view(),name='panel'),
    path('setup',views.setup.as_view(),name='setup'),
    path('home',views.home.as_view(),name='home'),
    path('create_company',views.create_company.as_view(),name='create_company'),
]
