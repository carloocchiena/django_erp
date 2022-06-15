from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'erp_core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('company_create/', login_required(views.CompanyCreate.as_view()), name='company_create'),
    path('invoice_create/', login_required(views.InvoiceCreate.as_view()), name='invoice_create'),
]