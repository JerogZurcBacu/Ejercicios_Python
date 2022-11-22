## Clase
class Coche():
    ## Constructor
    def __init__(self):     
    ## Propiedades
        self.largoChasis=250
        self.anchoChasis=100
        ## Encapsulado de variable
        self.__ruedas=4
        self.enMarcha=False
    ##Metodos
    def Arrancar(self, arrancamos):
        self.enMarcha=arrancamos
        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()
        if (self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta detenido"

    def Estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Unancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

    ## Encapulado de Metodos
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

##Instanciar una clase
miCoche=Coche()
print(miCoche.Arrancar(True))
miCoche.Estado()
print("------------- A continuacion creamos el segundo objeto-------------------")
miCoche=Coche()
print(miCoche.Arrancar(False))
miCoche.Estado()