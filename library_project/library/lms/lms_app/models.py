from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Book(models.Model):
    status_book=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title= models.CharField(max_length=80)
    author= models.CharField(max_length=80, null= True, blank=True)
    author_image= models.ImageField(upload_to='photos', null=True, blank= True)
    image= models.ImageField(upload_to='photos', null=True, blank= True)
    pages= models.IntegerField(null= True, blank= True)
    price= models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= True)
    rental_price= models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= True)
    rental_period= models.IntegerField(null= True, blank= True)
    totalprice=  models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= True)
    active= models.BooleanField(default= True)
    status= models.CharField(max_length= 50, choices=status_book, null= True, blank=True)
    category= models.ForeignKey(Category, on_delete= models.PROTECT)

    def __str__(self):
        return self.title
