from django.contrib import admin
from .models import FoodPage
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('id','infoname')
    list_display_links = ('id','infoname')
    list_per_page = 25
    search_fields = ('infoname',)

admin.site.register(FoodPage,PageAdmin)