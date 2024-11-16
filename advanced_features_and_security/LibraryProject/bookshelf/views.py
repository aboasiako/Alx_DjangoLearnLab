from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Document
from django.shortcuts import render
from .models import Book 

@permission_required('your_app_name.can_create', raise_exception=True)
def create_document(request):
    # Logic to create a document
    pass

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    # Logic to edit a document
    pass

@permission_required('your_app_name.can_view', raise_exception=True)
def view_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'document_detail.html', {'document': document})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    document.delete()
    return redirect('document_list')

def book_list(request):
    books = Book.objects.all()  # Fetch all book objects
    return render(request, 'bookshelf/book_list.html', {'books': books})

