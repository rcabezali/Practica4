from django.urls import path
from .views import (
    # Práctica 4: Vistas API
    registrar_biblioteca, listar_bibliotecas, detalles_biblioteca, registrar_libro, listar_libros_de_biblioteca, detalles_libro, actualizar_libro, eliminar_libro, filtrar_libros_disponibles, registrar_usuario, listar_usuarios, detalles_usuario, listar_prestamos_usuario, registrar_prestamo, listar_prestamos_activos, devolver_libro,
    # Práctica 6: Vistas web basadas en formularios
    nuevo_library, nuevo_book, nuevo_user, nuevo_loan,
    # Práctica 6: Extras
    lista_bibliotecas_web, detalle_biblioteca_web
)

urlpatterns = [
    # --- Práctica 4: API REST (JSON) ---
    # Gestión de Bibliotecas
    path('libraries/registrar/', registrar_biblioteca, name='registrar_biblioteca'),
    path('libraries/', listar_bibliotecas, name='listar_bibliotecas'),
    path('libraries/<int:biblioteca_id>/', detalles_biblioteca, name='detalles_biblioteca'),

    # Gestión de Libros
    path('books/registrar/', registrar_libro, name='registrar_libro'),
    path('libraries/<int:biblioteca_id>/books/', listar_libros_de_biblioteca, name='listar_libros_de_biblioteca'),
    path('books/<int:libro_id>/', detalles_libro, name='detalles_libro'),
    path('books/<int:libro_id>/actualizar/', actualizar_libro, name='actualizar_libro'),
    path('books/<int:libro_id>/eliminar/', eliminar_libro, name='eliminar_libro'),
    path('books/disponibles/', filtrar_libros_disponibles, name='filtrar_libros_disponibles'),

    # Gestión de Usuarios
    path('users/registrar/', registrar_usuario, name='registrar_usuario'),
    path('users/', listar_usuarios, name='listar_usuarios'),
    path('users/<int:usuario_id>/', detalles_usuario, name='detalles_usuario'),
    path('users/<int:usuario_id>/loans/', listar_prestamos_usuario, name='listar_prestamos_usuario'),

    # Gestión de Préstamos
    path('loans/registrar/', registrar_prestamo, name='registrar_prestamo'),
    path('loans/', listar_prestamos_activos, name='listar_prestamos_activos'),
    path('loans/<int:prestamo_id>/devolver/', devolver_libro, name='devolver_libro'),

    # --- Práctica 6: Interfaz Web usando formularios ---
    # Crear Biblioteca
    path('web/libraries/nuevo/', nuevo_library, name='nuevo_library'),
    # Listar Biblioteca
    path('web/libraries/', lista_bibliotecas_web, name='lista_bibliotecas_web'),
    # Consultar detalles Biblioteca
    path('web/libraries/<int:biblioteca_id>/', detalle_biblioteca_web, name='detalle_biblioteca_web'),
    # Crear Libro
    path('web/books/nuevo/', nuevo_book, name='nuevo_book'),
    # Registrar Usuario
    path('web/users/nuevo/', nuevo_user, name='nuevo_user'),
    # Registrar Préstamo
    path('web/loans/nuevo/', nuevo_loan, name='nuevo_loan'),
]
