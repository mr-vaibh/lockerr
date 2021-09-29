from django.contrib import admin

from .models import LongUrl

# Register your models here.

@admin.register(LongUrl)
class LongUrlAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url', 'description', 'created_at')