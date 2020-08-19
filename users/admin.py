from django.contrib import admin

from users.models import Profile, Choices

admin.site.register(Profile)
admin.site.register(Choices)