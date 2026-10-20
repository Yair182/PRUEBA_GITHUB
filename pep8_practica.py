#creamos la clase padre


class Vehiculo:

        #metodo construtor
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
       
        #metodo propios
    def mostrar_informacion(self):
        print(self.__dict__.items())

    def acelerar(self):
        print(f"aumentando de 0 a {self.velocidad}km/h.")


# CLASE HIJA -> Problablemente necesite una mejora Perrita
#clase hija
class Auto(Vehiculo):

        #construtor con atributo propio de la clase hija 
    def __init__(self, marca, modelo, velocidad, numero_puertas):
        self.numero_puertas = numero_puertas
        super().__init__(marca, modelo, velocidad)

        #metodo propio
    def tocar_bocina(self):
        print("bing biing🔊")


#asignacion de datos 
carro = Auto(
    marca="Toyota",
    modelo="4x4",
    velocidad="120km/h",
    numero_puertas= "4")


carro.mostrar_informacion()
carro.acelerar()
carro.tocar_bocina()


#clase hija 
class Motocicleta(Vehiculo):

        #construtor con atributo propio de la clase hija 
    def __init__(self, marca, modelo, velocidad,cilindraje):
        self.cilindraje = cilindraje
        super().__init__(marca, modelo, velocidad)
        print("hola")

        #metodo propio
    def caballito(self):
        print("estas andando en 1 rueda. WOW!")


#asignacion de datos 
moto = Motocicleta(
	marca = "kawasaki",
    modelo = "deportiva",
    velocidad = "100km/h",
    cilindraje = "450cc")

print("hola")
moto.mostrar_informacion()
moto.acelerar()
moto.caballito()

