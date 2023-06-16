from django.contrib import admin
from .models import *
from .models import Item
# Register your models here.
@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')