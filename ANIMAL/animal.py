class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        print(f'{self.nombre} esta comiendo')

    def dormir(self):
        print(f'{self.nombre} esta duermiendo')

    def hacer_sonido(self):
        print(f'{self.nombre} esta haciendo sonidos')

