from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Library, Book, User, Loan

# Práctica 6:
from django.shortcuts import render, redirect
from .forms import LibraryForm, BookForm, UserForm, LoanForm


# Gestión de Bibliotecas

@csrf_exempt
def registrar_biblioteca(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            biblioteca = Library.objects.create(
                name=data['name'],
                address=data['address']
            )
            return JsonResponse({"mensaje": "Biblioteca registrada con éxito", "biblioteca_id": biblioteca.id})
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_bibliotecas(request):
    if request.method == 'GET':
        bibliotecas = list(Library.objects.values())
        return JsonResponse(bibliotecas, safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalles_biblioteca(request, biblioteca_id):
    if request.method == 'GET':
        try:
            biblioteca = Library.objects.values("id", "name", "address").get(id=biblioteca_id)
            return JsonResponse(biblioteca)
        except Library.DoesNotExist:
            return JsonResponse({"error": "Biblioteca no encontrada"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Gestión de Libros

@csrf_exempt
def registrar_libro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            biblioteca = Library.objects.get(id=data['library_id'])
            if not data.get('title'):
                return JsonResponse({"error": "El título no puede estar vacío"}, status=400)
            libro = Book.objects.create(
                library=biblioteca,
                title=data['title'],
                author=data['author'],
                isbn=data.get('isbn')
            )
            return JsonResponse({"mensaje": "Libro registrado con éxito", "libro_id": libro.id})
        except Library.DoesNotExist:
            return JsonResponse({"error": "Biblioteca no encontrada"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_libros_de_biblioteca(request, biblioteca_id):
    if request.method == 'GET':
        libros = list(Book.objects.filter(library_id=biblioteca_id)
                      .values("id", "title", "author", "isbn", "available"))
        return JsonResponse(libros, safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalles_libro(request, libro_id):
    if request.method == 'GET':
        try:
            libro = Book.objects.values("id", "title", "author", "isbn", "available", "library_id").get(id=libro_id)
            return JsonResponse(libro)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Libro no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def actualizar_libro(request, libro_id):
    if request.method in ['PUT', 'PATCH']:
        try:
            libro = Book.objects.get(id=libro_id)
            data = json.loads(request.body)
            if 'title' in data:
                if not data['title']:
                    return JsonResponse({"error": "El título no puede estar vacío"}, status=400)
                libro.title = data['title']
            if 'author' in data:
                libro.author = data['author']
            if 'isbn' in data:
                libro.isbn = data['isbn']
            if 'available' in data:
                libro.available = data['available']
            libro.save()
            return JsonResponse({"mensaje": "Libro actualizado con éxito"})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Libro no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_libro(request, libro_id):
    if request.method == 'DELETE':
        try:
            libro = Book.objects.get(id=libro_id)
            libro.delete()
            return JsonResponse({"mensaje": "Libro eliminado con éxito"})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Libro no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def filtrar_libros_disponibles(request):
    if request.method == 'GET':
        available_param = request.GET.get('available', None)
        if available_param is not None:
            if available_param.lower() == 'true':
                libros = Book.objects.filter(available=True).values("id", "title", "author", "isbn", "library_id")
            elif available_param.lower() == 'false':
                libros = Book.objects.filter(available=False).values("id", "title", "author", "isbn", "library_id")
            else:
                return JsonResponse({"error": "El parámetro 'available' debe ser true o false"}, status=400)
            return JsonResponse(list(libros), safe=False)
        else:
            libros = Book.objects.values("id", "title", "author", "isbn", "available", "library_id")
            return JsonResponse(list(libros), safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Gestión de Usuarios

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = User.objects.create(
                name=data['name'],
                email=data['email']
            )
            return JsonResponse({"mensaje": "Usuario registrado con éxito", "usuario_id": usuario.id})
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = list(User.objects.values())
        return JsonResponse(usuarios, safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalles_usuario(request, usuario_id):
    if request.method == 'GET':
        try:
            usuario = User.objects.values("id", "name", "email").get(id=usuario_id)
            return JsonResponse(usuario)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_prestamos_usuario(request, usuario_id):
    if request.method == 'GET':
        try:
            usuario = User.objects.get(id=usuario_id)
            prestamos = list(usuario.loans.values())
            return JsonResponse(prestamos, safe=False)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Gestión de Préstamos

@csrf_exempt
def registrar_prestamo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            libro = Book.objects.get(id=data['book_id'])
            usuario = User.objects.get(id=data['user_id'])
            prestamo = Loan.objects.create(
                book=libro,
                user=usuario
            )
            return JsonResponse({"mensaje": "Préstamo registrado con éxito", "prestamo_id": prestamo.id})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Libro no encontrado"}, status=404)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except ValidationError as ve:
            return JsonResponse({"error": str(ve)}, status=400)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_prestamos_activos(request):
    if request.method == 'GET':
        prestamos = list(Loan.objects.filter(active=True).values())
        return JsonResponse(prestamos, safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def devolver_libro(request, prestamo_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body) if request.body else {}
            prestamo = Loan.objects.get(id=prestamo_id)
            prestamo.active = False
            prestamo.return_date = data.get('return_date', timezone.now())
            prestamo.save()
            prestamo.book.available = True
            prestamo.book.save()
            return JsonResponse({"mensaje": "Libro devuelto con éxito"})
        except Loan.DoesNotExist:
            return JsonResponse({"error": "Préstamo no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


# Vistas práctica 6: Para crear nuevas entidades mediante formularios
# 1. Biblioteca
def nuevo_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = LibraryForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nueva Biblioteca'})

# 2. Libro
def nuevo_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data.get('title'):
                form.add_error('title', "El título no puede estar vacío")
            else:
                form.save()
                return redirect('listar_libros_de_biblioteca', biblioteca_id=form.cleaned_data.get('library').id)
    else:
        form = BookForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo Libro'})

# 3. Usuario
def nuevo_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UserForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo Usuario'})

# 4. Préstamo
def nuevo_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_prestamos_activos')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = LoanForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo Préstamo'})