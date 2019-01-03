from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','is_mvp','phone','email')
    list_display_links = ('name',)
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
