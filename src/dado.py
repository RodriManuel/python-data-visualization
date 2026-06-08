import random as rd

class Dado:
    """Esta clase representa un simple dado."""
    
    def __init__(self, cant_lados=6):
        """El valor por defecto es para un dado de 6 lados."""
        self.cant_lados = cant_lados

    def get_lados(self):
        return self.cant_lados
    
    def tirar(self):
        """Retorna un valor aleatorio entre 1 y la cantidad de lados."""
        return rd.randint(1, self.get_lados())