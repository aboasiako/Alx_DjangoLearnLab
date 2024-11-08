# query_samples.py in relationship_app

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Access related books using the related_name
        return books
    except Author.DoesNotExist:
        return f"No author found with name '{author_name}'"

def list_all_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Access related books through ManyToMany relation
        return books
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Access related librarian through OneToOne relation
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"
    except Librarian.DoesNotExist:
        return f"No librarian found for library '{library_name}'"

# Example usage for testing in a Django context
if __name__ == "__main__":
    # Replace these names with actual data present in your database for testing
    author_name = "Author Name"
    library_name = "Library Name"

    print("Books by Author:")
    books_by_author = query_books_by_author(author_name)
    for book in books_by_author:
        print(book)

    print("\nBooks in Library:")
    books_in_library = list_all_books_in_library(library_name)
    for book in books_in_library:
        print(book)

    print("\nLibrarian for Library:")
    librarian = retrieve_librarian_for_library(library_name)
    print(librarian)
