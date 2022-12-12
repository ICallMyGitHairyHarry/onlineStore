from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from basket.models import Order, Prod_list
from registration.models import Customer, Adm


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'


class AdmInline(admin.StackedInline):
    model = Adm
    can_delete = False
    verbose_name_plural = 'adms'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline, AdmInline,)


class ProdlistInline(admin.TabularInline):
    model = Prod_list
    can_delete = False
    verbose_name_plural = 'adms'


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProdlistInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
