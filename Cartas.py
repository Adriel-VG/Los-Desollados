
class Personaje:
    def __init__(self, vida, fuerza, defensa):
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        
    def golpear(self, enemigo):
        print(f"Golpeas a {enemigo.nombre} y le haces {self.fuerza} puntos de daño")
        enemigo.vida -= self.fuerza
        print(f"A {enemigo.nombre} le quedan {enemigo.vida} puntos de salud")
        

class Enemigo:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def golpear(self):
        print(f" te ha golpeado, recibes {self.fuerza} puntos de daño")

Javier = Personaje(100, 3, 5)
Manuel = Enemigo("Manuel",30, 3)

Javier.golpear(Manuel)
