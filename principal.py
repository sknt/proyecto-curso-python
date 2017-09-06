#!/usr/bin/python3
#

# Voy a empezar por crear una biblioteca de ejemplo
biblioteca = []

def crea_libro(titulo, autor, editorial, anno_publicacion = None): # Por hacer: implementar campos adicionales, como el del año.
    """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}

# Para empezar, voy a meter dos sagas de libros. Esto podría ser la inicialización de la clase que será finalmente.
hp = []
hp.append(crea_libro("Harry Potter y la piedra Filosofal", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y la cámara secreta", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el prisionero de Azkaban", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el cáliz de fuego", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y la Orden del Fénix", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el misterio del príncipe", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y las reliquias de la muerte", "J. K. Rowling", "Salamandra"))

fundacion = []
fundacion.append(crea_libro("Fundación", "Isaac Asimov", "Cenit"))
fundacion.append(crea_libro("Fundación e Imperio", "Isaac Asimov", "Cenit"))
fundacion.append(crea_libro("Segunda Fundación", "Isaac Asimov", "Cenit"))

biblioteca = biblioteca + hp + fundacion

def muestra_repertorio():
    for i in range(len(biblioteca)):
        libro = biblioteca[i]
        print(str(i) + ". " + libro["Título"] + ", " + libro["Autor"] + ", " + libro["Editorial"] + ".")

muestra_repertorio()

def agrega_libro():
    """Interactúa con el usuario para permitirle agregar un libro a la biblioteca."""
    titulo = input("Introduzca el título del libro: ")
    autor = input("Introduzca el nombre del autor: ")
    editorial = input("Introduzca el nombre de la editorial: ")
    
    biblioteca.append(crea_libro(titulo, autor, editorial))

agrega_libro()

muestra_repertorio()
