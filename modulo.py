#!/usr/bin/python3
#

def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si lo es y vuelve a pedir uno si no."""
    while type(i) != int:
        try:
            i = int(i)
        except ValueError:
            i = input(in_numero)
    return i



def crea_libro(titulo, autor, editorial):
    """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}





# Creo una biblioteca de ejemplo
biblioteca = []

# Para empezar, voy a meter dos sagas de libros. Esto podría ser la inicialización de la clase que será finalmente.
hp = []
hp.append(crea_libro("Harry Potter y la piedra filosofal", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y la cámara secreta", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el prisionero de Azkaban", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el cáliz de fuego", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y la Orden del Fénix", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y el misterio del príncipe", "J. K. Rowling", "Salamandra"))
hp.append(crea_libro("Harry Potter y las Reliquias de la Muerte", "J. K. Rowling", "Salamandra"))

fundacion = []
fundacion.append(crea_libro("Fundación", "Isaac Asimov", "Cenit"))
fundacion.append(crea_libro("Fundación e Imperio", "Isaac Asimov", "Cenit"))
fundacion.append(crea_libro("Segunda Fundación", "Isaac Asimov", "Cenit"))

biblioteca = biblioteca + hp + fundacion
