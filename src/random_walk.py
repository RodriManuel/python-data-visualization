import random as rd

class RandomWalk:
    """"Esta clase genera un Random Walk."""
    def __init__(self, number_points=1000):
        """"Atributos de un Random Walk."""
        self.number_points = number_points

        # Cada camino comienza en las posiciones: (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_x_values(self):
        return self.x_values
    
    def get_y_values(self):
        return self.y_values

    def trazar_camino(self):
        """Genera cada punto del camino."""
        while len(self.x_values) < self.number_points:
            # Determina una posición aleatoria para avanzar.
            x_direction = rd.choice([1, -1])
            x_distance = rd.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = rd.choice([1, -1])
            y_distance = rd.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Ignora los pasos que no avanzan.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula una nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Agrega la nueva posición a las listas de posiciones.
            self.x_values.append(x)
            self.y_values.append(y)
