# Update a Book Instance

## Command
```bash
book= Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
```