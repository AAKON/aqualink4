from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'career'

urlpatterns = [

    path('',views.career,name='career'),
    path('career_details/<int:job_id>',views.career_details,name='career_details'),
    path('cv_submit',views.cv_email,name='cv_email'),
    


]
