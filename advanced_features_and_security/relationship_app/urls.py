# relationship_app/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import list_books, LibraryDetailView 


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    
    # URL for the class-based view to display library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
