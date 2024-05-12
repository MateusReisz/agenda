from django.db import models
from django.utils import timezone
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

=======

# Create your models here.

>>>>>>> c122867318f46906d42adccd4206e0b53e5ad538

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
<<<<<<< HEAD
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True)
=======
    
>>>>>>> c122867318f46906d42adccd4206e0b53e5ad538

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'