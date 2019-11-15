from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.

class Profile(models.Model):
    bio = HTMLField()
    avatar = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return  

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile 

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile 

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile              