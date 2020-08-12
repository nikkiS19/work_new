"""
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from datetime import datetime

from paywix.payu import Payu

#confuguring the stripe account
Payu.api_key = settings.PAYU_MERCHANT_KEY #not sure about this line

MEMBERSHIP_CHOICES = (
    ('Free','free'),
    ('Paid', 'paid')
)

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES,
    default='Free',
    max_length=30)
    price = models.IntegerField(default=15)
    Payu_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    #one to one bcz we have only one user membership for the user
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Payu_customer_id = models.CharField(max_length=40)       
    membership = models.ForeignKey(Membership,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership, created = UserMembership.objects.get_or_create(user=instance)

    if user_membership.Payu_customer_id is None or user_membership.Payu_customer_id == '':
        #this will just create a customer on stripe backend
        new_customer_id = Payu.customer.create(email=instance.email)   
        user_membership.Payu_customer_id = new_customer_id['id']
        user_membership.save()
post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership,on_delete=models.CASCADE)
    Payu_susbcription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
"""