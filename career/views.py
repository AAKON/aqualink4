from django.shortcuts import render
import datetime
from django.utils.timezone import get_current_timezone
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from .models import Career_description
from .forms import UploadFileForm
# Create your views here.

def career(request):
    today = datetime.datetime.now(tz=get_current_timezone())
    career_description = Career_description.objects.filter(deadline__range=[today,datetime.datetime.max])
    job_openings = len(career_description)
    return render(request,'career/career.html',{'job_openings':job_openings,'career_description':career_description})

def career_details(request,job_id):
    career_description = Career_description.objects.filter(pk=job_id)
    return render(request,'career/career_detailes.html',{'career_description':career_description})

def cv_email(request):
    pdf = request.FILES['pdf']
    
    designation = request.POST['designation']
    
    subject, from_email, to = 'Career:'+designation, 'website@aqualinkbd.xyz', 'website@aqualinkbd.xyz'
    text_content = 'Please check the attached file.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach('cv.pdf',pdf.read(),'application/pdf')
    msg.send()

    messages.info(request, "Thank you for submitting your resume")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    