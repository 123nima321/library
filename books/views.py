from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book


def book_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    books = Book.objects.all()
    
    if query:
        books = books.filter(title__icontains=query)
    
    if category:
        books = books.filter(category=category)
    
    categories = Book.objects.values_list('category', flat=True).distinct()
    
    context = {
        'books': books,
        'categories': categories,
        'selected_category': category,
        'search_query': query,
    }
    
    return render(request, 'books/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
