from django.contrib import admin

from lend_assist.models import Category, Service
from lend_assist.models import Neighbour, Request

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Neighbour)
admin.site.register(Request)
