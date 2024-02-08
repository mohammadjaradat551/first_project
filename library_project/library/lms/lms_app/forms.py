from django import forms
from .models import Book, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= [
            'name',
        ]
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

class BookForm(forms.ModelForm):
    class  Meta:
        model = Book
        fields=  [
            'title',
            'author',
            'author_image',
            'image',
            'pages',
            'price',
            'rental_price',
            'rental_period',
            'totalprice',
            'status',
            'category',
        ]
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'author_image': forms.FileInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price': forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'rental_period': forms.NumberInput(attrs={'class':'form-control','id':'rentalperiod'}),
            'totalprice': forms.NumberInput(attrs={'class':'form-control','id':'totalprice'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }