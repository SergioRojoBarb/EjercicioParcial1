
#Todas harán referencia por eso podré usar super(), esta no usa self, lo único se añade a la clase claro está
#entre paréntesis la clase a la que refiere según las dos ramas que se crean en el diagrama de flujo del ejercicio

class vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class coche(vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return  super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
         
    
#c = coche("azul", 4, 150, 1200)
#print(c)

class camioneta(coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

#cam = camioneta("azul", 4, 150, 1200, 600)
#print(cam)

class bicicleta(vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return  super().__str__() + ", {} ".format(self.tipo)
         
    
#b = bicicleta("azul", 2, "urbana")
#print(b)

class motocicleta(bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

#m = motocicleta("azul", 2, "deportiva", 300, 1000)
#print(m)


#Función que me va a permitir catalogar, me devuelve el nombre de la clase con todo lo que acompañará que 
#pondré en una lista
def catalogar(vehiculos):
    for i in vehiculos:
        print(type(i).__name__, i)
        
#Hago bucle que recorra la lista inspeccionando el número de ruedas, si no hay ninguna pues el conteo==0, ahora
#si != 0 pues hay ruedas, mínimo 2, para contarlas metemos nuestro objeto i con un .ruedas que es igual al nº de
#ruedas que tenga el vehículo, se suman y se añaden con el .format en el print en el primer dic contador en el
#segundo ruedas
def catalogar(vehiculos, ruedas=None):

    if ruedas != None:
        contador = 0
        for i in vehiculos:
            if i.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(contador, ruedas))

#Bucle para printar los vehículos == al nombre de las clases y que por tanto saco con type(i).__name__, si no
#hay nº de ruedas printo los objetos que no tengan ruedas, si sí hay printo los que sí que tienen.
    for i in vehiculos:
        if ruedas == None:
            print(type(i).__name__, i)
        else:
            if i.ruedas == ruedas:
                print(type(i).__name__, i)
                

#Pongo en la lista mis clases y veo las variables que me pide meter en los paréntesis, relleno con los datos
#de arriba menos colores que antes eran siempre los mismos. Aunque eso da igual, la importancia la tendrá la
#segunda variable de la clase, las ruedas que es nuestro filtro.
       
lista = [
    coche("azul", 4, 150, 1200),
    camioneta("gris", 4, 150, 1200, 600),
    bicicleta("amarilla", 2, "urbana"),
    motocicleta("roja", 2, "deportiva", 300, 1000)
]

#Catalogo con la función según mi lista separado con una coma el número de ruedas que busco que es la condición
#seleccionada para dividir a los distintos vehiculos

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)
