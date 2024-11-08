from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Get the author by name
    books_by_author = Book.objects.filter(author=author)  # Filter books by the author
    return books_by_author

# List all books in a library
def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Get the library by name
    books_in_library = library.books.all()  # Access the books related to the library
    return books_in_library

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Get the library by name
    librarian = library.librarian  # Access the librarian related to the library
    return librarian
