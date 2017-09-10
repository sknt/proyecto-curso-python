#!/usr/bin/python3
#

from modulo import *

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



def comprueba_numero(i):
    """Comprueba si lo introducido por el usuario es un número y, si no, pide otro."""
    while haz_numero(i) == "No es un número": # Si no se puede convertir, pide otro hasta que se pueda
        i = input(in_numero)
    return haz_numero(i)



biblioteca = Biblioteca() # Creamos la biblioteca



def muestra_repertorio():
    """Muestra los libros que hay en la biblioteca."""
    for i, libro in enumerate(biblioteca.libros):
        print(str(i) + ". " + libro["Título"] + ", " + libro["Autor"] + ", " + libro["Editorial"] + ".")



def agrega_libro():
    """Interactúa con el usuario para permitirle agregar un libro a la biblioteca."""
    # Pide al usuario los datos necesarios
    titulo = input(in_titulo)
    autor = input(in_autor)
    editorial = input(in_editorial)
    
    biblioteca.agrega_libro(titulo, autor, editorial) # Llama al método que añade el libro a la biblioteca



def borra_libro():
    """Interactúa con el usuario para permitirle borrar un libro de la biblioteca."""
    muestra_repertorio()
    
    i = input(in_indice + in_libro + in_desee + in_borrar) # Pregunta qué libro borrar
    i = comprueba_numero(i)
    
    biblioteca.borra_libro(i) # Llama al método que borra el libro



def edita_libro():
    """Interactúa con el usuario para permitirle editar un libro de la biblioteca."""
    muestra_repertorio()
    
    i = input(in_indice + in_libro + in_desee + in_editar) # El usuario elige qué libro quiere editar
    i = comprueba_numero(i)
    
    # Muestra los campos del libro
    print("")
    for ii, campo in enumerate(biblioteca.campos): 
        print(str(ii) + ". " + campo + ": " + biblioteca.libros[i][campo] + ".")
    
    iii = input(in_indice + in_campo + in_desee + in_editar) # El usuario elige qué campo quiere editar del libro elegido
    iii = comprueba_numero(iii)
    
    biblioteca.edita_libro(i, biblioteca.campos[iii], input(in_nuevo)) # Llama al método que edita el campo



def interactua():
    """Interactúa con el usuario para realizar todas las acciones."""
    print(acciones) # Muestra las acciones
    i = input(in_indice + in_accion + in_desee + in_realizar) # Pregunta cuál es la que se quiere realizar
    print("\n\n\n")
    i = comprueba_numero(i)
    
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
