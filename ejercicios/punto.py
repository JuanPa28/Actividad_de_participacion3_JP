class Punto:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def mostrar(self):
        print(self.x , ",",self.y)
    def mover(self, new_punto):
        self.x = new_punto.x
        self.y = new_punto.y
    def calcular_distancia(self, punto_dado):
        distancia= (((punto_dado.x-self.x)**2)+((punto_dado.y-self.y)**2))**1/2
        return distancia



