from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","pkid","user","gender","country","city"]
    list_filter = ["gender","country","city"]
    list_display_links = ["id","pkid","user","gender","country","city"]

admin.site.register(Profile,ProfileAdmin)
