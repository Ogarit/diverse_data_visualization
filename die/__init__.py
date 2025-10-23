from random import randint


class Die:
    """Classe que representa um único dado."""

    def __init__(self, num_sides=6):
        """Faz a suposição de que um dado tem seis lados."""
        self.num_sides = num_sides

    def roll(self):
        """Retorna um valor aleatório entre 1 e o número de lados"""
        return randint(1, self.num_sides)
