#!/usr/bin/python3
#

# Cadenas usadas
numero_obligatorio = "Debe introducir un número: " # Usada cuando el usuario debía introducir un número y no lo hace
in_titulo = "Introduzca el título del libro: "
in_autor = "Introduzca el nombre del autor: "
in_editorial = "Introduzca el nombre de la editorial: "

in_indice = "Introduzca el índice que numera el libro que desee " # Usada cuando se le pide al usuario el número que corresponde a un libro al que se le quiera hacer alguna acción (ver las cadenas siguientes)
in_borrar = "borrar: "
in_editar = "editar: "


def haz_numero(i):
    """Comprueba si lo recibido es un número, transfórmalo si es y pide otro si no."""
    while type(i) != int:
        try:
            i = int(i)
        except ValueError:
            i = input(numero_obligatorio)
    return i

def crea_libro(titulo, autor, editorial, anno_publicacion = None): # TODO: implementar campos adicionales, como el del año.
    """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}





# Voy a crear una biblioteca de ejemplo
biblioteca = []

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
    titulo = input(in_titulo)
    autor = input(in_autor)
    editorial = input(in_editorial)
    
    biblioteca.append(crea_libro(titulo, autor, editorial))

def borra_libro(): # TODO: Controlar que no se salga del rango positivo de la lista y permitir cancelar (por ejemplo introduciendo -1)
    """Interactúa con el usuario para permitirle borrar un libro de la biblioteca."""
    i = input(in_indice + in_borrar)
    i = haz_numero(i)
    biblioteca.pop(i)

borra_libro()

muestra_repertorio()

#def edita_libro():
    #i = input(in_indice + in_editar)
