from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import *
from account.models import *

# Create your views here.
def initiate_subscription_payment(request: HttpRequest, pk) -> HttpResponse:
    if request.user.store_creator == True:
        store = Store.objects.get(store_name=request.user.store_name)
        subscription = Subscription.objects.get(pk=pk)
        if subscription.subscribers.filter(pk=store.pk).exists():
            return redirect("/")
        else:
            return render(
                request, "subscriptions/make-subscription-payments.html", 
                {"subscription": subscription, "store": store}
            )
    else:
        return redirect("/")

