from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'erp_core'

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'invoice', views.InvoiceViewSet)
router.register(r'payment', views.PaymentViewSet)

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    path('api/v1/', include(router.urls), name='api_v1'),
    path('help/', views.Help.as_view(), name='help'),
    path('feature/', views.Feature.as_view(), name='feature'),
    path('login/', auth_views.LoginView.as_view(template_name='erp_core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='erp_core/logout.html'), name='logout'),
    path('company_create/', login_required(views.CompanyCreate.as_view()), name='company_create'),
    path('company_list/', login_required(views.CompanyList.as_view()), name='company_list'),
    path('company_detail/<slug:slug>/', login_required(views.CompanyDetail.as_view()), name='company_detail'),
    path('company_update/<int:pk>/', login_required(views.CompanyUpdate.as_view()), name='company_update'),
    path('company_clone/<int:pk>/', login_required(views.CompanyClone.as_view()), name='company_clone'),
    path('product_create/', login_required(views.ProductCreate.as_view()), name='product_create'),
    path('product_list/', login_required(views.ProductList.as_view()), name='product_list'),
    path('product_detail/<int:pk>/', login_required(views.ProductDetail.as_view()), name='product_detail'),
    path('product_update/<int:pk>/', login_required(views.ProductUpdate.as_view()), name='product_update'),
    path('product_clone/<int:pk>/', login_required(views.ProductClone.as_view()), name='product_clone'),
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
    path('filtered_view/check_active/', login_required(views.CheckActive.as_view()), name='check_active'),
    path('filtered_view/check_passive/', login_required(views.CheckPassive.as_view()), name='check_passive'),
    path('csv_export/', login_required(views.CsvExport.as_view()), name='csv_export'),
]
