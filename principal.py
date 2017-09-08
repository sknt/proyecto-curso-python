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

acciones = "\n\n\nPuede realizar una de las siguientes acciones sobre la biblioteca:\n\n0. Ver la lista de libros.\n1. Agregar un nuevo libro.\n2. Borrar un libro.\n3. Editar un libro." # Texto inicial de la función interactiva


def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si lo es y vuelve a pedir uno si no."""
    while type(i) != int:
        try:
            i = int(i)
        except ValueError:
            i = input(in_numero)
    return i

def crea_libro(titulo, autor, editorial, anno_publicacion = None):
    """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
    return {"Título": titulo, "Autor": autor, "Editorial": editorial}

campos = ["Título", "Autor", "Editorial"]





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





def muestra_repertorio():
    """Muestra los libros que hay en la biblioteca."""
    for i, libro in enumerate(biblioteca):
        print(str(i) + ". " + libro["Título"] + ", " + libro["Autor"] + ", " + libro["Editorial"] + ".")

def agrega_libro():
    """Interactúa con el usuario para permitirle agregar un libro a la biblioteca."""
    # Pide al usuario los datos necesarios
    titulo = input(in_titulo)
    autor = input(in_autor)
    editorial = input(in_editorial)
    
    biblioteca.append(crea_libro(titulo, autor, editorial)) # Añade el libro a la biblioteca

def borra_libro():
    """Interactúa con el usuario para permitirle borrar un libro de la biblioteca."""
    muestra_repertorio()
    i = input(in_indice + in_libro + in_desee + in_borrar) # Pregunta qué libro borrar
    i = haz_numero(i)
    biblioteca.pop(i) # Borra el libro

def edita_libro():
    """Interactúa con el usuario para permitirle editar un libro de la biblioteca."""
    muestra_repertorio()
    
    i = input(in_indice + in_libro + in_desee + in_editar) # El usuario elige qué libro quiere editar
    i = haz_numero(i)
    
    print("")
    for ii, campo in enumerate(campos): # Muestra los campos del libro
        print(str(ii) + ". " + campo + ": " + biblioteca[i][campo] + ".")
    
    iii = input(in_indice + in_campo + in_desee + in_editar) # El usuario elige qué campo quiere editar del libro elegido
    iii = haz_numero(iii)
    
    biblioteca[i][campos[iii]] = input(in_nuevo) # El usuario edita el campo

def interactua():
    """Interactúa con el usuario para realizar todas las acciones."""
    print(acciones) # Muestra las acciones
    i = input(in_indice + in_accion + in_desee + in_realizar) # Pregunta cuál es la que se quiere realizar
    print("\n\n\n")
    i = haz_numero(i)
    
    # Ejecuta la acción elegida
    if i == 0:
        muestra_repertorio()
        input("")
    elif i == 1:
        agrega_libro()
    elif i == 2:
        borra_libro()
    elif i == 3:
        edita_libro()

while True: # Ejecutamos el programa interactivo en bucle
    interactua()
