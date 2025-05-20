class Enemigo:
    def init(self, nombre, vida, fuerza, exp):
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
            self.vida = 0
            print(f"Acabas de derrotar a {self.nombre} recibiste {self.exp} puntos de experiencia")
            global karma
            karma -= 1
        else:
            print(f"Ahora {self.nombre} tiene {self.vida} puntos de vida")

#Enemigos
Hormiga = Enemigo("Hormiga gigante",30, 3, 10)
