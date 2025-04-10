from electrico import TipoElectrico

class Raichu(TipoElectrico):
    def __init__(self, defensa=50, ataque=55):
        super().__init__("Raichu", defensa, ataque)
