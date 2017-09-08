#!/usr/bin/python3
#

# Cadenas usadas
in_numero = "Debe introducir un número: " # Usada cuando el usuario debía introducir un número y no lo hace
in_titulo = "Introduzca el título del libro: "
in_autor = "Introduzca el nombre del autor: "
in_editorial = "Introduzca el nombre de la editorial: "
in_nuevo = "Introduzca el nuevo campo: "

in_indice = "\nIntroduzca el índice que numera " # Usada cuando se le pide al usuario el número que corresponde a algo a lo que se le quiera hacer alguna acción (ver las cadenas siguientes)
# Objetos
in_libro = "el libro "
in_campo = "el campo "
in_accion = "la acción "
# Común
in_desee = "que desee "
# Acciones
in_borrar = "borrar: "
in_editar = "editar: "
in_realizar = "realizar: "

acciones = "\n\n\nPuede realizar una de las siguientes acciones sobre la biblioteca:\n\n0. Ver la lista de libros.\n1. Agregar un nuevo libro.\n2. Borrar un libro.\n3. Editar un libro."


def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si es y pide otro si no."""
    while type(i) != int:
        try:
            i = int(i)
        except ValueError:
            i = input(in_numero)
    return i

def crea_libro(titulo, autor, editorial, anno_publicacion = None):
    """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}

lista_campos = ["Título", "Autor", "Editorial"]





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

#muestra_repertorio()

def agrega_libro():
    """Interactúa con el usuario para permitirle agregar un libro a la biblioteca."""
    titulo = input(in_titulo)
    autor = input(in_autor)
    editorial = input(in_editorial)
    
    biblioteca.append(crea_libro(titulo, autor, editorial))

def borra_libro():
    """Interactúa con el usuario para permitirle borrar un libro de la biblioteca."""
    muestra_repertorio()
    i = input(in_indice + in_libro + in_desee + in_borrar)
    i = haz_numero(i)
    biblioteca.pop(i)

#borra_libro()

#muestra_repertorio()

def edita_libro():
    """Interactúa con el usuario para permitirle editar un libro de la biblioteca."""
    muestra_repertorio()
    
    i = input(in_indice + in_libro + in_desee + in_editar) # El usuario elige qué libro quiere editar
    i = haz_numero(i)
    
    print("")
    for ii, campo in enumerate(lista_campos):
        print(str(ii) + ". " + campo + ": " + biblioteca[i][campo] + ".")
    
    iii = input(in_indice + in_campo + in_desee + in_editar) # El usuario elige qué campo quiere editar del libro elegido
    iii = haz_numero(iii)
    
    biblioteca[i][lista_campos[iii]] = input(in_nuevo)

#edita_libro()

#muestra_repertorio()

def interactua():
    print(acciones)
    i = input(in_indice + in_accion + in_desee + in_realizar)
    print("\n\n\n")
    i = haz_numero(i)
    
    if i == 0:
        muestra_repertorio()
        input("")
    elif i == 1:
        agrega_libro()
    elif i == 2:
        borra_libro()
    elif i == 3:
        edita_libro()

while True:
    interactua()
