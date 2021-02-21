# instancias
class Coordenada:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def distancia(self, segunda_coordenada: object) -> float:
        x_dif = (self.x - segunda_coordenada.x)**2
        y_dif = (self.y - segunda_coordenada.y)**2

        return (x_dif + y_dif)**0.5

if __name__ == "__main__":
    coordenada1 = Coordenada(1,30)
    coordenada2 = Coordenada(3,40)
    print(coordenada1.distancia(coordenada2))
    print(isinstance(coordenada2,Coordenada))
    print(isinstance(3,Coordenada))

