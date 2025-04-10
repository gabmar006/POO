from mamifero import Mamifero
from oviparo import Oviparo
from venenoso import Venenoso

class Ornitorrinco(Mamifero, Oviparo, Venenoso):
    '''a diferencia del uso de interfaces en java en python
    no se requiere implementar los metodos de las clases'''
    def __init__(self, nombre, edad):
        '''LLama al constructor de la clase mamifero, la primera
        base determinada por el MRO'''
        super().__init__(nombre, edad)
        self.NUMERO_HUEVOS=0