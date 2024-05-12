from django.contrib import admin
from contact.models import Contact
<<<<<<< HEAD
from contact import models
=======
>>>>>>> c122867318f46906d42adccd4206e0b53e5ad538

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id','first_name', 'last_name', 'phone', 'email', 'show')
=======
    list_display = ('id','first_name', 'last_name', 'phone', 'email',)
>>>>>>> c122867318f46906d42adccd4206e0b53e5ad538
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
<<<<<<< HEAD
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'phone', 'email',

@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
=======
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone', 'email',
>>>>>>> c122867318f46906d42adccd4206e0b53e5ad538
