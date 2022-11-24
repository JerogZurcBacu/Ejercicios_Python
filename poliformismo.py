class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
    
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 reudas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamient()

miVehiculo=Camion
desplazamientoVehiculo(miVehiculo)