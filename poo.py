## Clase
class Coche():
    ## Propiedades
    largoChasis=250
    anchoChasis=100
    ruedas=4
    enMarcha=False
    ##Metodos
    def Arrancar(self):
        self.enMarcha=True
    def Estado(self):
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

##Instanciar una clase
miCoche=Coche()

print("El largo del chasis de miCcoche es: ", miCoche.largoChasis)
miCoche.Arrancar()
print(miCoche.Estado())