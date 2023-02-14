from ejercicios.punto import Punto
class Rectangulo:
    def _init_(self, punto1:Punto, punto2:Punto, colorlinea, colorfondo):
        self.punto_1: Punto = punto1
        self.punto_2: Punto = punto2
        self.color_linea = colorlinea
        self.color_fondo = colorfondo

    def calcular_area(self)->float:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)

        return base * altura

    def calcular_perimetro(self)->float:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)

        return (base + altura) * 2

    def es_cuadrado(self)->bool:
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)

        return base == altura
