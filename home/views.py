from django.shortcuts import render
from aqualink.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Home_top_div
from .models import Clients_div
from .models import About_div
from .models import Services_div
from .models import Product
from .models import Faq
from .models import Features
from .models import How_works
from .models import Overview
from .models import Video_product
from .models import Specification
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def home(request):

#get all the data for home page 

    top_div = Home_top_div.objects.all()
    clients = Clients_div.objects.all()
    about_us = About_div.objects.all()
    services_div = Services_div.objects.all()
    products = Product.objects.all()

    if 'product' not in request.session:
        request.session['product'] = []
    request.session['product_order'] = len(request.session['product'])

#this get request is for general purpose 

    if request.method == 'GET':

        return render(request,'home/index.html', {'top_div':top_div,'clients':clients,
                                                'about_us':about_us,'services_div':services_div,
                                                'products':products,
                                            })

#this post request for sending email

    elif request.method == 'POST':

        data = request.POST.copy()
        subject = data.get('subject')
        message = data.get('message')+data.get('email')+data.get('name')

        send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
        success = 'good to go'
        return render(request,'home/index.html', {'top_div':top_div,'clients':clients,
                                                'about_us':about_us,'services_div':services_div,
                                                'products':products,'success':success,
                                            })


def product(request,product_id):

#get all the data for specifict product details

    product_details = Product.objects.filter(pk = product_id)
    faqs = Faq.objects.filter(product_id = product_id)
    features = Features.objects.filter(product_id = product_id)
    overview = Overview.objects.filter(product_id = product_id)
    how_works = How_works.objects.filter(product_id = product_id)
    video_product = Video_product.objects.filter(product_id = product_id)
    specification = Specification.objects.filter(product_id = product_id)
    products = Product.objects.all()


    if 'product' not in request.session:
        request.session['product'] = []
    request.session['product_order'] = len(request.session['product'])

    return render(request,'product/product_details.html', {'product_details':product_details,
                                                            'faqs':faqs,'features':features,
                                                            'overview':overview,'how_works':how_works,
                                                            'video_product':video_product,'specification':specification,
                                                            "products":products,
                                                            })



def email(request):

    data = request.POST.copy()
    subject = data.get('subject')
    message = data.get('message')+'%0A'+data.get('name')+'%0A'+data.get('email')
    send_mail(
    subject,
    message,

    'website@aqualinkbd.xyz',
    ['website@aqualinkbd.xyz'],
    fail_silently=False,
                )
#after sending message this message will show on the specific page. 'django.contrib.messages' this the destination of this message. 
#it lives in setting.py/installed app

    messages.info(request, "Thank you, we will contact with you.")
    return HttpResponseRedirect("/")


