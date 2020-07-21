from django.contrib import admin
from .models import Home_top_div
from .models import Clients_div
from .models import About_div
from .models import Services_div
from .models import Product
from .models import Faq
from .models import Features
from .models import Overview
from .models import How_works
from .models import Video_product
from .models import Specification

# Register your models here.

admin.site.register(Home_top_div)
admin.site.register(Clients_div)
admin.site.register(About_div)
admin.site.register(Services_div)
admin.site.register(Product)
admin.site.register(Faq)
admin.site.register(Features)
admin.site.register(Overview)
admin.site.register(How_works)
admin.site.register(Video_product)
admin.site.register(Specification)
