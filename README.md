# Prácticas 4 y 6: Gestión de Libros en una Biblioteca

Prácticas 4 y 6 de ArqSoft, y pues nada un buen listado de toodas las rutas que si no me hago un lío.

- **Práctica 4: API REST:** Se comunica en formato JSON para realizar operaciones CRUD.
- **Práctica 6: Interfaz Web:** Basada en formularios y templates HTML (con Bootstrap), permite interactuar de forma visual con la aplicación.

## Rutas de la Aplicación

### API (REST - JSON)

#### Gestión de Bibliotecas
- **POST** `/libraries/registrar/`  
  Registra una nueva biblioteca. (Datos: `name`, `address`)
- **GET** `/libraries/`  
  Lista todas las bibliotecas.
- **GET** `/libraries/<biblioteca_id>/`  
  Muestra los detalles de una biblioteca específica.

#### Gestión de Libros
- **POST** `/books/registrar/`  
  Registra un nuevo libro asignado a una biblioteca. (Datos: `library_id`, `title`, `author`, opcional: `isbn`)
- **GET** `/libraries/<biblioteca_id>/books/`  
  Lista los libros de una biblioteca.
- **GET** `/books/<libro_id>/`  
  Consulta los detalles de un libro.
- **PUT/PATCH** `/books/<libro_id>/actualizar/`  
  Actualiza los datos de un libro.
- **DELETE** `/books/<libro_id>/eliminar/`  
  Elimina un libro.
- **GET** `/books/disponibles/?available=true|false`  
  Filtra los libros por disponibilidad.

#### Gestión de Usuarios
- **POST** `/users/registrar/`  
  Registra un nuevo usuario. (Datos: `name`, `email`)
- **GET** `/users/`  
  Lista todos los usuarios.
- **GET** `/users/<usuario_id>/`  
  Consulta los detalles de un usuario.
- **GET** `/users/<usuario_id>/loans/`  
  Lista los préstamos de un usuario.

#### Gestión de Préstamos
- **POST** `/loans/registrar/`  
  Registra un préstamo de un libro a un usuario. (Datos: `book_id`, `user_id`)
- **GET** `/loans/`  
  Lista los préstamos activos.
- **PUT** `/loans/<prestamo_id>/devolver/`  
  Marca un préstamo como finalizado, actualizando la disponibilidad del libro.

### Interfaz Web (formularios y templates)

#### Gestión de Bibliotecas (Web)
- **GET** `/web/libraries/nuevo/`  
  Muestra el formulario para crear una nueva biblioteca.
- **GET** `/web/libraries/`  
  Página de listado de todas las bibliotecas.
- **GET** `/web/libraries/<biblioteca_id>/`  
  Página de detalle de una biblioteca, que muestra los libros asociados.

#### Gestión de Libros (Web)
- **GET** `/web/books/nuevo/`  
  Muestra el formulario para crear un nuevo libro.
- **GET** `/web/books/`  
  Lista todos los libros.
- **GET** `/web/books/<libro_id>/`  
  Muestra el detalle de un libro (incluye información de disponibilidad).
- **GET/POST** `/web/books/<libro_id>/editar/`  
  Muestra y procesa el formulario para editar un libro.
- **GET/POST** `/web/books/<libro_id>/eliminar/`  
  Muestra una confirmación y procesa la eliminación de un libro.

#### Gestión de Usuarios (Web)
- **GET** `/web/users/nuevo/`  
  Muestra el formulario para registrar un nuevo usuario.
- **GET** `/web/users/`  
  Página de listado de usuarios.
- **GET** `/web/users/<usuario_id>/`  
  Muestra el detalle de un usuario, incluyendo su historial de préstamos.

#### Gestión de Préstamos (Web)
- **GET** `/web/loans/nuevo/`  
  Muestra el formulario para registrar un nuevo préstamo.
- **GET** `/web/loans/`  
  Lista los préstamos activos.
- **GET** `/web/users/<usuario_id>/loans/`  
  Muestra el historial de préstamos de un usuario.
- **GET/POST** `/web/loans/<prestamo_id>/devolver/`  
  Muestra la confirmación y procesa la devolución de un préstamo.