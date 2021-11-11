class Car:

        def move_to(self, pos_x, pos_y):
            self.pos_x = pos_x
            self.pos_y = pos_y
        def move_incr(self, x, y):
            self.pos_x += x
            self.pos_y += y
        def get_pos():
            return self.pos_x, self.pos_y
        def __init__(self, marca, modelo, combustible, cilindrada, pos_x, pos_y):
            self.marca = marca
            self.modelo = modelo
            self.combustible = combustible
            self.cilindrada = cilindrada
            self.pos_x = 0
            self.pos_y = 0

