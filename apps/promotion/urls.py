from django.urls import path
from . import views

app_name = 'promotion'

urlpatterns = [
    path('', views.voucher_list, name='voucher_list'),
    path('single_voucher/<slug:slug>/',views.single_voucher, name='single_voucher'),
    path('customer_redeem_voucher/<slug:slug>/',views.customer_redeem_voucher, name='customer_redeem_voucher'),
    path('redeem_voucher/<slug:slug>/',views.redeem_voucher, name='redeem_voucher'),
    path('package_list/', views.package_list, name='package_list'),
]