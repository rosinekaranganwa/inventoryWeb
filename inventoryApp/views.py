from django.shortcuts import render,redirect
from .forms import CreateBookForm

def create_book(request):
    if request.method=='POST':
        form=CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        
    else:
        form=CreateBookForm()
    return render(request,'books/create_book.html',{'form':form})

