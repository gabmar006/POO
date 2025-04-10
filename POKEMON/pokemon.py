class Pokemon:
    def __init__(self, nombre, defensa, ataque, tipo = "N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.tipo = tipo

    def __str__(self):
        #return f"{self.nombre} ({self.tipo})"
        tipo_emojis = {
        "Fuego": "🔥",
        "Agua": "🌊",
        "Hierba": "🌱",
        "Eléctrico": "⚡",
        "Hielo": "❄️",
        "Lucha": "🥊",
        "Veneno": "☠️",
        "Tierra": "🌬️",
        "Volador": "💸",
        "Psíquico": "🔮",
        "Bicho": "🐛",
        "Roca": "🪨",
        "Fantasma": "👻",
        "Dragón": "🐉",
        "Siniestro": "💀",
        "Acero": "🪦",
        "Hada": "🌸"
    }


    def _str_(self):
        emoji = self.tipo_emojis.get(self.tipo, "❓")
        return f"{self.nombre} ({self.tipo} {emoji})"
