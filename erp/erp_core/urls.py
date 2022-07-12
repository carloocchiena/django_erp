from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'erp_core'

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    path('help/', views.Help.as_view(), name='help'),
    path('login/', auth_views.LoginView.as_view(template_name='erp_core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='erp_core/logout.html'), name='logout'),
    path('company_create/', login_required(views.CompanyCreate.as_view()), name='company_create'),
    path('company_list/', login_required(views.CompanyList.as_view()), name='company_list'),
    path('company_detail/<slug:slug>/', login_required(views.CompanyDetail.as_view()), name='company_detail'),
    path('company_update/<int:pk>/', login_required(views.CompanyUpdate.as_view()), name='company_update'),
    path('invoice_create/', login_required(views.InvoiceCreate.as_view()), name='invoice_create'),
    path('invoice_list/', login_required(views.InvoiceList.as_view()), name='invoice_list'),
    path('invoice_update/<int:pk>/', login_required(views.InvoiceUpdate.as_view()), name='invoice_update'),
    path('payment_create/', login_required(views.PaymentCreate.as_view()), name='payment_create'),
    path('payment_list/', login_required(views.PaymentList.as_view()), name='payment_list'),
    path('payment_update/<int:pk>/', login_required(views.PaymentUpdate.as_view()), name='payment_update'),
    path('filtered_view/', login_required(views.FilteredView.as_view()), name='filtered_view'),
    path('filtered_view/invoice_active/', login_required(views.InvoiceActive.as_view()), name='invoice_active'),
    path('filtered_view/invoice_active_overdue/', login_required(views.InvoiceActiveOverdue.as_view()), name='invoice_active_overdue'),
    path('filtered_view/invoice_passive/', login_required(views.InvoicePassive.as_view()), name='invoice_passive'),
    path('filtered_view/invoice_passive_overdue/', login_required(views.InvoicePassiveOverdue.as_view()), name='invoice_passive_overdue'),
    path('filtered_view/payment_active/', login_required(views.PaymentActive.as_view()), name='payment_active'),
    path('filtered_view/payment_passive/', login_required(views.PaymentPassive.as_view()), name='payment_passive'),
    path('filtered_view/active_check/', login_required(views.ActiveCheck.as_view()), name='active_check'),
    path('filtered_view/passive_check/', login_required(views.PassiveCheck.as_view()), name='passive_check'),
]