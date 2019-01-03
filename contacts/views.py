from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Contact
from datetime import datetime
from django.contrib import messages



# Create your views here.
# test


def contact(request):
    
    if request.method == 'POST':
        print("Hello hasnian") 
        
        name =    request.POST['name']
        message = request.POST['message']
        email =   request.POST['email']
        listing = request.POST['listing_inquiry']
        phone =   request.POST['phone']
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']

        if Contact.objects.all().filter(user_id=user_id,listing_id=listing_id).exists():
            messages.error(request, 'Your have already inquired for this property. A realtor will soon get in touch with you') 

        else: 
            contact = Contact(  listing = listing, listing_id=listing_id, name= name,
                                email=email, phone=phone, message=message,
                                user_id=user_id )
            contact.save()
            messages.success(request, 'Your inquiry has been subimtted')



    return redirect('/listings/'+listing_id)
