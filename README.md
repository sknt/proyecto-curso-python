# Proyecto final del [curso de Python Darwin Eventur](http://www.darwineventur.com/2017/06/python-para-la-ingenieria-y-la-ciencia-online.html)
Este es simplemente el repositorio en el que voy a ir colgando todo mi trabajo final del curso ya que quería aprovechar para hacerlo usando `git` y así también practicar con ello.

Por favor, ten en cuenta que el repositorio original [está en BitBucket](https://bitbucket.org/josealberto4444/proyecto-curso-python). Aunque intentaré mantener actualizada también esta copia en GitHub, no prometo nada.

## Descripción
El proyecto consiste en diseñar un pequeño gestor de bibliotecas. Se trata de un programa que permita agregar libros a una colección, listarlos, modificarlos y quitarlos de ella.

### Requisitos mínimos (v0.1)
Al iniciar el programa, este debe permitir elegir una acción de entre las siguientes:

-   Mostrar lista.
-   Agregar libro.
-   Borrar libro.
-   Editar (modificar) libro.

Naturalmente, Cada una de las acciones debe permitir ejecutar la tarea correspondiente.

Cada libro debe tener

-   Autor.
-   Titulo.
-   Editorial.

El código debe estar acompañado de comentarios explicando el uso de cada función, etc.

### Posibles funcionalidades opcionales
Se sugieren las siguientes ideas:

-   Las funciones del programa relacionadas con la operativa interna deberían estar en un módulo aparte, y las relacionadas con la interfaz en el cuerpo principal. (v0.2)
-   Guardar los datos de la biblioteca en un archivo (un CSV, por ejemplo) y cargarlos al inicio, para que se conserven entre una ejecución y otra. (v0.3)
-   Control de errores (libros sin título, libros repetidos, etc.).
-   Permitir búsquedas por autor y editorial.
