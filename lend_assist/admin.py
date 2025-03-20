from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from lend_assist.models import Category, Service
from lend_assist.models import Neighbour, Request


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(Neighbour)
class NeighbourAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("phone", "address",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("address", "phone", "service",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "address",
                        "phone",
                        "service",
                    )
                },
            ),
        )
    )

admin.site.register(Service)
admin.site.register(Request)
