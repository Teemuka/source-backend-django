from django.contrib import admin
from .models import *

# Register your models here.


def created_by(obj):
    return "%s" % obj.created_by.username


@admin.register(NewsText)
class NewsTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', created_by)


@admin.register(Happening)
class HappeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', created_by)


created_by.short_description = "Created By"
