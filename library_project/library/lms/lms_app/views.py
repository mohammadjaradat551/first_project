from django.shortcuts import render
from .models import *
from .forms import BookForm, CategoryForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    #to save in database
    if request.method == 'POST':
        add_book= BookForm(request.POST, request.FILES)
        
        if add_book.is_valid():
            add_book.save()
        add_category= CategoryForm(request.POST)
        
        if add_category.is_valid():
            add_category.save()
    


    context= {
        'categorys': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'catForm': CategoryForm(),
        'allbooks':Book.objects.filter(active= True).count,
        'soldbook':Book.objects.filter(status= 'sold').count,
        'rentalbook':Book.objects.filter(status= 'rental').count,
        'availablebook':Book.objects.filter(status= 'available').count,


    }
    return render(request, 'pages/index.html', context)

def books(request):
    result= Book.objects.all()
    title= request.GET['search_name']
    result= result.filter(title__icontains=title)

    context= {
        'categorys':Category.objects.all(),
        'books': result,
        'catForm': CategoryForm(),
    }

    return render(request, 'pages/books.html', context)

def delete(request, id):
    book_id= Book.objects.get(id= id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')

def update(request, id):
    book_id= Book.objects.get(id=id)
    if request.method == 'POST':
        book_save= BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid:
            book_save.save()
            return redirect('/')# when pass to save, go to index page direct
    else :
        book_save= BookForm(instance=book_id)# ı dont understend
    context= {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context)
