from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# from random import randint
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Food(models.Model):
    item = models.CharField(max_length=200)
    calories = models.IntegerField()

    class Meta:
        ordering = ('item',)

class UserCalorie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=100, null=True,blank=True, default='')
    calories = models.CharField(max_length=100, null=True,blank=True, default='')
    owner = models.ForeignKey('auth.User',null=True,default=1,related_name ='estimate', on_delete=models.CASCADE)
    # related name  http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    
