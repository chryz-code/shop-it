from cmath import log
from distutils.log import error
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from account.models import *
from app.models import *
from .forms import *
from account.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from account.tokens import account_activation_token
# Create your views here.

def customer_register(request, slugified_store_name):
    if request.user.is_authenticated:
        logout(request)
    form = CustomerForm
    store = Store.objects.get(slugified_store_name=slugified_store_name)
    slugified_store_name = store.slugified_store_name
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.store = store
            email= form.cleaned_data["email"]
            check_email = User.objects.filter(email = email)
            if check_email:
                error = "You have an exiting account"
                return redirect("customer:existing_user_customer_register", slugified_store_name)
            else:
                user = User.objects.create(
                    email= form.cleaned_data["email"],
                    full_name=form.cleaned_data["full_name"],
                    is_active = False,
                    is_staff = False,
                    store_creator = False,
                )
                user.set_password(form.cleaned_data["password"])
                user.save()
                store.customers.add(user)
                customer.user = user
                customer.save()
                current_site = get_current_site(request)
                subject = "Activate your Shop!t Account"
                message = render_to_string(
                    "account/registration/account_activation_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                user.email_user(subject=subject, message=message)
                return render(request, "account/registration/registration-success.html")
    return render(request, "customer/register.html", {"store": store, "slugified_store_name": slugified_store_name, "form": form})

def customer_login(request, slugified_store_name):
    context = {}
    store = Store.objects.get(slugified_store_name=slugified_store_name)
    slugified_store_name = store.slugified_store_name
    if request.user.is_authenticated:
        logout(request)
        return redirect("customer:customer_login", slugified_store_name=slugified_store_name)


    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(email=email)
        if user:
            user = authenticate(request, email=email, password=password)
            if user:
                if user in store.customers.all():
                    login(request, user)
                    return redirect("app:store" , slugified_store_name=store.slugified_store_name)
                else:
                    messages.error(request, "You are not a customer of this store.")
            else:
                messages.error(request, "Password is incorrect")            
        else:
            messages.error(request, "User does not exist")
    
    return render(request, "customer/login.html", {"store": store, "slugified_store_name": slugified_store_name})

def existing_user_customer_register(request, slugified_store_name):
    form = ExistingUserCustomerForm
    store = Store.objects.get(slugified_store_name=slugified_store_name)
    slugified_store_name = store.slugified_store_name
    if request.method == "POST":
        form = ExistingUserCustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)
            if user not in store.customers.all():
                form.save(commit=False)
                customer = Customer.objects.create(
                    user = user,
                    full_name = user.full_name,
                    email = user.email,
                    password = user.password,
                    password2 = user.password,
                    store = store.store_name,
                )
                customer.save()
                store.customers.add(user)
                return redirect("customer:customer_login", slugified_store_name=slugified_store_name)
            else:
                messages.error(request, "You are already a customer of this store.")

    return render(request, "customer/existing-user-register.html", {"store": store, "slugified_store_name": slugified_store_name, "form": form})

def customer_logout(request, slugified_store_name):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    logout(request)
    return redirect("app:store" , slugified_store_name=store.slugified_store_name)

def customer_product_detail(request, slugified_store_name, slug):
        store = Store.objects.get(slugified_store_name=slugified_store_name)
        product = get_object_or_404(Product, created_by=store.store_name, slug=slug)
        category_product = Product.objects.filter(
            category=product.category, created_by= store.store_name
        ).exclude(id=product.id)[:6]
        return render(
            request,
            "product/product-detail.html",
            {"product": product, "category_product": category_product, 'store':store},
        )

def customer_profile(request, slugified_store_name):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    if request.user in store.customers.all():
        account = Customer.objects.get(store=store.store_name, email=request.user)
        if account:
            userprofileform = UserProfileForm(instance=account)
            if request.method == "POST":
                userprofileform = UserProfileForm(request.POST, request.FILES, instance=account)
                if userprofileform.is_valid():
                    userprofileform.save()
                    return redirect("/")

            return render(
                request,
                "customer/customer-profile.html",
                {"userprofileform": userprofileform, "account": account, 'store':store},
            )
        else:
            return redirect("customer:customer_login", slugified_store_name=slugified_store_name)
    else:
        logout(request)
        return redirect("customer:customer_login", slugified_store_name=slugified_store_name)

def customer_wishlist(request, slugified_store_name):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    user = request.user
    wishlist = Product.objects.filter(wishlist=user)
    return render(request, "customer/customer-wishlist.html", {"wishlist": wishlist, "store": store})

def address_list(request, slugified_store_name):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    customer = Customer.objects.get(email=request.user.email)
    address_list = Address.objects.filter(customer=customer).order_by('-default')
    return render(request, "customer/address-list.html", {"address_list": address_list, "store": store})

def create_address(request, slugified_store_name):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    customer = Customer.objects.get(email=request.user.email)
    default_address = Address.objects.filter(customer=customer, default= True)
    address_form = AddressForm()
    if request.method == "POST":
        address_form = AddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = customer
            if default_address:
                address_form.default = False
                address_form.save()
                return redirect("customer:address_list", slugified_store_name=slugified_store_name)
            else:
                address_form.default = True
                address_form.save()
                return redirect("customer:address_list", slugified_store_name=slugified_store_name)
    return render(request, "customer/address-create.html", {"address_form": address_form, "store": store})

def edit_address(request, slugified_store_name, id):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    customer = Customer.objects.get(email= request.user.email)
    address = get_object_or_404(Address, id=id, customer=customer)
    address_form = AddressForm(instance=address)
    if request.method == "POST":
        address_form = AddressForm(request.POST, instance=address)
        if address_form.is_valid():
            address_form.save()
            return redirect("customer:address_list", slugified_store_name=slugified_store_name)
    return render(request, "customer/address-create.html", {"address_form": address_form, "store": store})

def delete_address(request, slugified_store_name, id):
    store = get_object_or_404(Store, slugified_store_name= slugified_store_name)
    customer = Customer.objects.get(email= request.user.email)
    address = get_object_or_404(Address, id=id, customer=customer)
    address.delete()
    return redirect("customer:address_list", slugified_store_name=slugified_store_name)

def set_default_address(request, slugified_store_name, id):
    store = get_object_or_404(Store, slugified_store_name=slugified_store_name)
    customer = Customer.objects.get(email=request.user.email)
    Address.objects.filter(customer=customer, default=True).update(default=False)
    Address.objects.filter(id=id, customer=customer).update(default=True)
    previous_url = request.META.get("HTTP_REFERER")
    return redirect("customer:address_list", slugified_store_name=slugified_store_name)


def customer_add_wishlist(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    store = get_object_or_404(Store, store_name = product.created_by)
    product.wishlist.add(user)
    return redirect("customer:customer_wishlist", slugified_store_name= slugify(store))


def customer_remove_wishlist(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    store = get_object_or_404(Store, store_name = product.created_by)
    product.wishlist.remove(user)
    return redirect("app:product_detail", slug=product.slug, slugified_store_name= slugify(store))

def customer_stores(request):
    customer = User.objects.get(email=request.user.email, store_creator=False, store_staff=False)
    if customer:
        stores = Store.objects.filter(customers=customer)
        return render(request, "customer/customer-stores.html", {"stores": stores})

  




        

