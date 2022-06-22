import secrets

from django.db import models

from account.models import *
from .paystack import Paystack


# Create your models here.
class Duration(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    ref = models.CharField(max_length=200, blank=True, null=True)
    verified = models.BooleanField(default=False)
    subscribers = models.ManyToManyField(
        Store, related_name="subscriptions", blank=True
    )
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.duration.name)

    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            objects_with_similar_ref = Subscription.objects.filter(ref=ref)
            if not objects_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)




class Subscription_Timeline(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mail_remainder = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subscription ) + ' ' + str(self.store.store_name) + ' ' + 'timeline'


class RecurringSubscriptionData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    authorization_code = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user.full_name) + " " + str(self.user.store_name) + " " + str(self.amount)