from django.contrib import admin

from . import models
from .models import UserProfile,ProfileFeedItem
from django.contrib.auth.admin import UserAdmin
'''Register your models here.'''
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
# admin.site.register(UserProfileManager)
