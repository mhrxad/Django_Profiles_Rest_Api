from django.contrib import admin
from profiles_api_app import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
