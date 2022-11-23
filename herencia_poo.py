##--- Ejemplo Herencia ---##

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

##Herencia
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
        ## Sobreescritura de metodos 
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, " \nHabilidad: ", self.hcaballito)

class VElectricos():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True

## Herencia Multiple (Se da preferencia a la primer herencia VElectricos)
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miMoto=Moto("Honda", "CBR")
miMoto.estado()
miBici=BicicletaElectrica()
