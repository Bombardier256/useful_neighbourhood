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
        (("Additional info", {"fields": ("address", "phone",)}),)
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


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        "name", "date", "complete", "category", "reward", "description",
    ]
    search_fields = ["name", "description"]
    list_filter = ["category", "date"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "name", "category", "is_lending", "free_of_charge", "price", "description",
    ]
    search_fields = ["name", "description"]
    list_filter = ["category", "is_lending"]


#admin.site.register(Manufacturer)