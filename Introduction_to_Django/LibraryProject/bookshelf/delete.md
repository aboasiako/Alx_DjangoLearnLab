# Delete a Book Instance

## Command
```bash
book= Book.objects.get(title="1984")
book.delete()

#To comfrim Deletion
books=Book.objects.all()
print(books)