# LibraryProject

## We start by setting up Django Development Environment
1. **Install Django**:
```bash 
pip install django
```
2. **Create and start Django**:
```bash
django-admin startproject LibraryProject
```
3. **Run the Development Environment**:
```bash
cd LibraryProject
```
Create a README.md file in LIbraryProject
```bash 
touch README.md
```
-run then development server using: 
```bash
python manage.py runserver
```
 - Open a web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the default Django welcome page.

4. **Explore the Project Structure**:
Familiarize yourself with created project structure and pay attention to:
**settings.py**: Configuration for the Django project.

**urls.py**: The URL declarations for the project; a “table of contents” of your Django-powered site.
**manage.py**: A command-line utility that lets you interact with this Django project
