from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateBookForm
from .models import *

def index(request):
    return render(request,'books/index.html')

def create_book(request):
    if request.method=='POST':
        form=CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form=CreateBookForm()
    return render(request,'books/create_book.html',{'form':form})


def list_books(request):
    books = CreateBook.objects.all()
    return render(request, 'books/list_books.html', {'books': books})

def update_book(request, pk):
    book = get_object_or_404(CreateBook, pk=pk)
    if request.method == 'POST':
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = CreateBookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form, 'book': book})

def delete_book(request, pk):
    book = get_object_or_404(CreateBook, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'books/delete_book.html', {'book': book})
