from importlib.resources import Package
from django.shortcuts import redirect, render
from django.urls import reverse

from apps.promotion.models import Voucher

# Create your views here.
def voucher_list(request):
    voucher= Voucher.objects.all()
    return render(request,'voucher_list.html',{'voucher' : voucher})

def single_voucher(request,slug):
    voucher= Voucher.objects.get(slug=slug)
    link = request.build_absolute_uri(reverse('promotion:redeem_voucher', kwargs={"slug": voucher.slug}))
    print(voucher.package_name.image)
    return render(request,'voucher_details.html',{'voucher' : voucher, "link":link})


def redeem_voucher(request,slug):
    Can_redeem = False
    if request.user.is_authenticated:
        Can_redeem = True
    
    voucher= Voucher.objects.get(slug=slug)
    return render(request,'voucher_redeem.html',{'voucher' : voucher, 'canredeem':Can_redeem })

def customer_redeem_voucher(request,slug):
    
    voucher = Voucher.objects.filter(slug=slug)
    voucher.update(
        redeemed_by = request.user, redeemed_status = True
    )
    

    return redirect('promotion:redeem_voucher', slug=slug)


def package_list(request):
    package = Package.objects.all()
    return render(request,'package_list.html',{'package' : package})
