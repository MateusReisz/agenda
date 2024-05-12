from django.contrib import admin
from contact.models import Contact
from contact import models

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone', 'email', 'show')
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'phone', 'email',

@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',