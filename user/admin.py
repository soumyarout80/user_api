from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Account, AccountDetail, Manager
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    # To Display in Admin page
    list_display = ("id", 'first_name', 'middle_name', 'last_name', 'password', 'email',
                    'phone', 'gender', 'created_at', 'modified_at', 'expiry')

    readonly_fields = ['id', 'created_at', 'modified_at']

    # To Edit fields in Admin page
    fields = ('first_name', 'middle_name', 'last_name', 'password', 'email',
              'phone', 'gender', 'expiry')

    # To Filter by first_name in Admin page
    list_filter = ["first_name"]

    ordering = ['id']
    # This will add a search box to the screen
    # The __startswith modifier restricts the search to last names that begin with the search parameter.
    search_fields = ("first_name__startswith",)


@admin.register(AccountDetail)
class AccountDetailsAdmin(admin.ModelAdmin):
    # To Display in Admin page
    list_display = ('account', 'title', 'description', 'state', 'country',
                    'zip_code', 'status')

    readonly_fields = ['account']

    # To Edit fields in Admin page
    fields = ('account', 'title', 'description', 'state', 'country',
              'zip_code', 'status',)

    # To Filter by first_name in Admin page
    list_filter = ['account']

    ordering = ['account', 'title']

    # This will add a search box to the screen
    # The __startswith modifier restricts the search to last names that begin with the search parameter.
    search_fields = ("first_name__startswith",)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    # To Display in Admin page
    list_display = ('account', 'manager_name', 'manager_email', 'manager_phone')

    readonly_fields = ['account']

    # To Edit fields in Admin page
    fields = ('account', 'manager_name', 'manager_email', 'manager_phone')

    # To Filter by first_name in Admin page
    list_filter = ['account']

    ordering = ['account', 'manager_name']

    # This will add a search box to the screen
    # The __startswith modifier restricts the search to last names that begin with the search parameter.
    search_fields = ("first_name__startswith",)