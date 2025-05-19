

#Variables
balas = 5
karma = 0
#CLASES
    #Clases de personajes
class Personaje:
    def __init__(self, vida, fuerza, defensa):
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        
    def golpear(self, enemigo):
        print(f"Golpeas a {enemigo.nombre} y le haces {self.fuerza} puntos de daño")
        enemigo.vida -= self.fuerza
        print(f"A {enemigo.nombre} le quedan {enemigo.vida} puntos de salud")
        
    #Clases de enemigos
class Enemigo:
    def __init__(self, nombre, vida, fuerza, exp):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.exp = exp

    def golpear(self):
        print(f" te ha golpeado, recibes {self.fuerza} puntos de daño")

    def muerte(self):
        if self.vida <=0:
            self.vida = 0
            print(f"Felicidades acabas de derrotar a {self.nombre} recibiste {self.exp} puntos de experiencia")
            global karma
            karma += 1
        else:
            print(f"Ahora {self.nombre} tiene {self.vida} puntos de vida")

    def muerte_karma(self):
        if self.vida <=0:
            self.vida == 0
            print(f"Acabas de derrotar a {self.nombre} recibiste {self.exp} puntos de experiencia")
            global karma
            karma -= 1
        else:
            print(f"Ahora {self.nombre} tiene {self.vida} puntos de vida")

    #Clases de Armas
class CartaBalas:
    def __init__ (self, nombre, fuerzaExtra):
        self.nombre = nombre
        self.fuerzaExtra = fuerzaExtra

    def usar_bala(self, enemigo, personaje):
        global balas
        balas -= 1
        if balas <= 0:
            print("No cuentas con balas")
        else:
            print(f"Haz usado {self.nombre} ")
            daño_total = self.fuerzaExtra + personaje.fuerza
            print(f"Hiciste {daño_total}")
            enemigo.vida-= daño_total
            enemigo.muerte()
            print(f"Te quedan {balas} balas")
            

#PERSONAJES
    #Protagonistas
Javier = Personaje(100, 3, 5)
Caballo = Personaje(200, 6, 10)

    #Enemigos
MariquitaInfect = Enemigo("Mariquita Infectada",30, 3, 10)



#CARTAS
    #Cartas de Balas
bala_Normal = CartaBalas("Bala", 7)

bala_Normal.usar_bala(MariquitaInfect, Javier)
