from ejercicios.punto import Punto
class Circulo:
    def __init__(self, centro:Punto, radio):
        self.centro:Punto = centro
        self.radio = radio
    def calcular_area(self)->float:
        area= 3.1416*(self.radio)**2
        return area
    def calcular_perimetro(self)->float:
        perimetro= 2*(3.1416*(self.radio)**2)
    def punto_pertenece_al_circulo(self, new_punto):
        ecuacion_p=(((self.centro.x - new_punto.x)**2) + ((self.centro.y - new_punto.y)**2))**1/2

        return ecuacion_p==self.radio**2