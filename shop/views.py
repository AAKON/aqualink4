from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Product
from .models import Shop
from .models import oder_tb
from .models import Oder_item
import json
from django.contrib import messages
from .utils import render_to_pdf
import datetime
from django.core.mail import EmailMultiAlternatives



# Create your views here.

def shop(request):

#this post from search inbox
    if request.method == 'POST':

        word=request.POST['key_word']
        products = Product.objects.filter(name__icontains = word)
        product_price = request.POST['price_range']
        
    else:
        products = Product.objects.all()
    price = Shop.objects.all()

#checking if any cart information exists for this user
    if 'product' not in request.session:
        request.session['product'] = []

#how many types of products selected by this user
    products_in_cart = set(request.session['product'])

    request.session['product_order'] = len(request.session['product'])

#this one for quantity 
    quantity = request.session['product']
    cart={}
    for product in products_in_cart:
        order=0
        for q in quantity:
            if q==product:
                order=order+1

        cart.update({product:order})

    cart_product = Product.objects.filter(pk__in=products_in_cart)
    print(cart_product)

    return render(request,'shop/shop.html',{'products':products,'prices':price,'cart_item':cart,'cart_products':cart_product})



def cart(request):

    products = Product.objects.all()
    price = Shop.objects.all()
    if 'product' not in request.session:
        request.session['product'] = []
    products_in_cart = set(request.session['product'])
    request.session['product_order'] = len(request.session['product'])
    quantity = request.session['product']
    cart={}
    for product in products_in_cart:
        order=0
        for q in quantity:
            if q==product:
                order=order+1

        cart.update({product:order})

    cart_product = Product.objects.filter(pk__in=products_in_cart)
    # alert_color ='background-color:red; font-weight:bold; opacity:.5;color:white;'
    return render(request,'shop/cart.html',{'products':products,'prices':price,'cart_item':cart,
    'cart_products':cart_product})


def add_to_cart(request,pk):

    if 'product' not in request.session:
        request.session['product'] = []

    cart_list = request.session['product']
    cart_list.append(pk)
    request.session['product'] = cart_list
    request.session['product_order'] = len(cart_list)
    print(request.session['product'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request,pk):
    if 'product' not in request.session:
        request.session['product'] = []

    cart_list = request.session['product']
    cart_list.remove(pk)
    request.session['product'] = cart_list
    request.session['product_order'] = len(cart_list)
    print(request.session['product'])
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.info(request, "Item removed from your cart.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def order(request):
    quantity = request.POST['quantity'].split(',')
    pro = request.session['product']
    total_price = request.POST['total_price']
    vat = request.POST['vat']
    vat_total = request.POST['vat_total']
    products =Product.objects.filter(pk__in=pro)
    price = Shop.objects.all()
    em = request.POST['email']
    # print(vat)


    cutomer = oder_tb(
                customer_name = request.POST['name'],
                customer_address=request.POST['address'],
                customer_phone=request.POST['phone'],
                customer_email=request.POST['email']
    )
    cutomer.save()

    for idx,product in enumerate(pro):
        item = Oder_item(
        product_name=Product.objects.filter(pk=product).values('name'),
        product_id= product,
        product_quantity = quantity[idx],
        oder_tb_id = cutomer.pk
        )
        item.save()

    request.session['product'] = []
    request.session['product_order'] = len(request.session['product'])

    data = {
            'time': datetime.datetime.now(),
            'products_cart': products,
            'product_quantity': quantity,
            'product_price': price,
            'total_price' : total_price,
            'vat' : vat,
            'vat_total' : vat_total,
            'customer_name'  :  request.POST['name'],
            'customer_address' : request.POST['address'],
            'customer_phone' : request.POST['phone'],
            'customer_email' : request.POST['email'],
        }
#this one using shop/utils.py file to genarate pdf
    
    pdf = render_to_pdf('pdf/invoice.html', data)

#for sending email to customer
    subject, from_email, to = 'Your order from Aqualink shop', 'website@aqualinkbd.xyz', em
    text_content = 'Please check the attached file.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(pdf.getvalue(),'application/pdf')
    msg.send()

#for sending email to our end
    subject, from_email, to = 'New cutomer order', 'website@aqualinkbd.xyz', 'website@aqualinkbd.xyz'
    text_content = 'Please check the attached file.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(pdf.getvalue(),'application/pdf')
    msg.send()

#this one for message feedback
    messages.info(request, "Successfully placed your order, soon we will contact with you. Check your email,which you just submitted. Thank you !")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponse(pdf.getvalue(), content_type='application/pdf')

def quotation(request):
    quantity = request.POST['quantity'].split(',')
    pro = request.session['product']
    total_price = request.POST['total_price']
    vat = request.POST['vat']
    vat_total = request.POST['vat_total']
    products =Product.objects.filter(pk__in=pro)
    price = Shop.objects.all()
    em = request.POST['email']


    data = {
            'time': datetime.datetime.now(),
            'products_cart': products,
            'product_quantity': quantity,
            'product_price': price,
            'total_price' : total_price,
            'vat' : vat,
            'vat_total' : vat_total,
            'customer_name'  :  request.POST['name'],
            'customer_address' : request.POST['address'],
            'customer_phone' : request.POST['phone'],
            'customer_email' : request.POST['email'],
        }
#this one using shop/utils.py file to genarate pdf
   
    pdf = render_to_pdf('pdf/quotation.html', data)

#for sending email to customer
    subject, from_email, to = 'Your quotation from Aqualink shop', 'website@aqualinkbd.xyz', em
    text_content = 'Please check the attached file.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(pdf.getvalue(),'application/pdf')
    msg.send()

#for sending email to our end
    subject, from_email, to = 'New cutomer quotation', 'website@aqualinkbd.xyz', 'website@aqualinkbd.xyz'
    text_content = 'Please check the attached file.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(pdf.getvalue(),'application/pdf')
    msg.send()

#this one for message feedback
    messages.info(request, "Please check your email for quotation,which you just submitted. Thank you !")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponse(pdf.getvalue(), content_type='application/pdf')

