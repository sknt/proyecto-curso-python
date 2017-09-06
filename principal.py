#!/usr/bin/python3
#

# Voy a empezar por crear una biblioteca de ejemplo
biblioteca = []

def crea_libro(titulo, autor, editorial, anno_publicacion = None): # Por hacer: implementar campos adicionales, como el del año. También comentar esta función bien con docstrings
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}

# Para empezar, voy a meter dos sagas de libros
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
