from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView


# Function-based view to list all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    
    # Render the 'list_books.html' template and pass the books to it
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include all books in the library in the context
        library = self.get_object()
        context['books'] = library.books.all()  # Assumes a reverse relationship from Library to Book
        return context
