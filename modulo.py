#!/usr/bin/python3
#

def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si lo es y devuelve una cadena si no."""
    try:
        i = int(i)
        return i
    except ValueError:
        return "No es un número"





class Biblioteca: # TODO: ¡Comentar!
    
    campos = ["Título", "Autor", "Editorial"]
    libros = []
    
    def __init__(self):
        
        # Para empezar, voy a meter dos sagas de libros.
        hp = []
        hp.append(self.crea_libro("Harry Potter y la piedra filosofal", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y la cámara secreta", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y el prisionero de Azkaban", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y el cáliz de fuego", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y la Orden del Fénix", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y el misterio del príncipe", "J. K. Rowling", "Salamandra"))
        hp.append(self.crea_libro("Harry Potter y las Reliquias de la Muerte", "J. K. Rowling", "Salamandra"))

        fundacion = []
        fundacion.append(self.crea_libro("Fundación", "Isaac Asimov", "Cenit"))
        fundacion.append(self.crea_libro("Fundación e Imperio", "Isaac Asimov", "Cenit"))
        fundacion.append(self.crea_libro("Segunda Fundación", "Isaac Asimov", "Cenit"))
        
        self.libros = self.libros + hp + fundacion
    
    
    def crea_libro(self, titulo, autor, editorial):
        """Crea la estructura necesaria (un diccionario) para almacenar un libro en la biblioteca."""
        return {"Título": titulo, "Autor": autor, "Editorial": editorial}
    
    def agrega_libro(self, titulo, autor, editorial):
        """Añade el libro a la biblioteca."""
        self.libros.append(self.crea_libro(titulo, autor, editorial))
    
    def borra_libro(self, i):
        self.libros.pop(i)
    
    def edita_libro(self, libro, campo, valor):
        self.libros[libro][campo] = valor
