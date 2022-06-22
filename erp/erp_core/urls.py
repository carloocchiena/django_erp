from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'erp_core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='erp_core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='erp_core/logout.html'), name='logout'),
    path('company_create/', login_required(views.CompanyCreate.as_view()), name='company_create'),
    path('invoice_create/', login_required(views.InvoiceCreate.as_view()), name='invoice_create'),
    path('company_list/', login_required(views.CompanyList.as_view()), name='company_list'),
    path('invoice_list/', login_required(views.InvoiceList.as_view()), name='invoice_list'),
    path('company_detail/<slug:slug>/', login_required(views.CompanyDetail.as_view()), name='company_detail'),
    path('invoice_update/<int:pk>/', login_required(views.InvoiceUpdate.as_view()), name='invoice_update'),
    path('company_update/<int:pk>/', login_required(views.CompanyUpdate.as_view()), name='company_update'),
]