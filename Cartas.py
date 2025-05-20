class CartaBalas:
    def init (self, nombre, fuerzaExtra):
        self.nombre = nombre
        self.fuerzaExtra = fuerzaExtra
    def usar_bala(self, enemigo, personaje):
        global balas
        if balas <= 0:
            print("No cuentas con balas")
            balas = 0
        else:
            balas -=1
            print(f"Haz usado {self.nombre} ")
            daño_total = self.fuerzaExtra + personaje.fuerza
            print(f"Hiciste {daño_total} de daño")
            enemigo.vida-= daño_total
            enemigo.muerte()
            print(f"Te quedan {balas} balas")


#Cartas de Balas
bala_normal = CartaBalas("Bala", 7)
