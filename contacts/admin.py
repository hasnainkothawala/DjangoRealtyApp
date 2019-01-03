from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display =('listing','listing_id','name','email','phone','message','user_id')
    list_display_links =('listing','listing_id')
    search_fields = ('listing','listing_id','name','email','phone','message','user_id')
    list_per_page = 25



admin.site.register(Contact, ContactsAdmin)
