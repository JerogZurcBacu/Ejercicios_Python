## Archivo para distribucion de paquetes
import setuptools from setup

setup(
    name: "Paquete",
    version: "1.0"
    description: "Ejemplo de archivo de distribucion"
    author: "Jorge Cruz Garcia"
    author_email: "meuuniccoreu@gmail.com"
    URL: "www.jorgecg.tech"
    package: ["Calculos", "calculos.redondeo_potencia"]

)

## En terminal...
# python setup.py sdist

##Instalar
# pip3 install nombre_paquete.zip

##Desinstalar 
# pip3 uninstal nombre_paquete.zip

 