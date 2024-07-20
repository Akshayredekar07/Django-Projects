from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


# def books_view(request):
#     books_list=Book.objects.all()
#     return render(request, 'testapp/book.html', {'books_list': books_list})

# >> This are not required in CBV it is hidden

class BookListView(ListView):
    model=Book
    #default template files: book_list.html 
    # template_name='testapp/book.html'
    #default context object: book_list 
    # context_object_name="books"

class BookListView2(ListView):
    model=Book
    #default template files: book_list.html 
    template_name='testapp/book.html'
    #default context object: book_list 
    context_object_name="books"


class BookDetailView(DetailView):
    model=Book
    #default template fiel: book_detail.html
    #default context object: book or object


class BookCreateView(CreateView):
    model=Book
    fields=('title', 'author','pages','price')


class BookUpdateView(UpdateView):
    model=Book
    fields=('pages', 'price')
    #default template is 


class BookDeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('listbooks')
    
     