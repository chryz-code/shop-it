from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from app.models import *

from .cart import *
from app.forms import UseCouponForm
import time, datetime
from datetime import datetime, timedelta

from .cart import * 


# Create your views here.
def cart_summary(request):
    grand_total = ''
    form_feedback = ''
    cart = Cart(request)
    form = UseCouponForm
    if request.method == "POST":
        form = UseCouponForm(request.POST)
        if form.is_valid():
            coupon_code = form.cleaned_data.get("coupon")
            if Coupon.objects.filter(code=coupon_code).exists():
                coupon = Coupon.objects.get(code=coupon_code)
                if request.user not in coupon.users.all():
                    expiry_date = (datetime.now().astimezone() - coupon.created_at)
                    expiry_date_seconds = expiry_date.total_seconds()
                    minutes = expiry_date_seconds/60
                    if int(minutes) > coupon.expiry_date:
                        form_feedback = 'Copoun is Expired'
                    else:
                        coupon_percentage = coupon.percentage
                        cart.get_grand_total(coupon_percentage)
                        coupon.users.add(request.user)
                        grand_total = int(cart.get_grand_total(coupon_percentage))
                        form_feedback = 'Coupon Successfully Used'
                else:
                    form_feedback = 'Copoun has been used by you'
            else:
                form_feedback = 'Coupon does not exist'           
    return render(request, "cart/cart-summary.html", {"cart": cart, "form": form, "grand_total": grand_total, "form_feedback": form_feedback})
               

def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        product_qty = cart.__len__()
        response = JsonResponse({"qty": product_qty})
        return response


def delete_from_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({"qty": cartqty, "subtotal": carttotal})
        return response


def update_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        item_qty = int(request.POST.get("productqty"))
        cart.update(product=product_id, qty=product_qty, cartitemqty=item_qty)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        a_product_price = get_object_or_404(Product, id=product_id).price
        a_discount_price = get_object_or_404(Product, id=product_id).discount_price()
        
        if Product.objects.get(id=product_id).discount_price() < a_product_price:
            cartproductqty = item_qty * a_discount_price
        else:
            cartproductqty = item_qty * Decimal(a_product_price)
        print(cartproductqty)
        response = JsonResponse(
            {"qty": cartqty, "subtotal": carttotal, "cartproqty": cartproductqty}
        )
        return response


def clear_all_cart(request):
    cart = Cart(request)
    cart.clear()
    cartqty = cart.__len__()
    carttotal = cart.get_total_price()
    response = JsonResponse({"qty": cartqty, "subtotal": carttotal})
    return redirect("/cart/", response)
