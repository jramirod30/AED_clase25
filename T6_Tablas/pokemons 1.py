from typing import Dict, Tuple

# Diccionario de Pokémon: nombre → info (vida, ataque, defensa, tipo)
pokemon: Dict[str, Dict[str, int | str]] = {
    "Pikachu": {
        "vida": 100,
        "ataque": 55,
        "defensa": 10,
        "tipo": "eléctrico⚡"
    },
    "Charmander": {
        "vida": 100,
        "ataque": 52,
        "defensa": 14,
        "tipo": "fuego🔥"
    },
    "Squirtle": {
        "vida": 100,
        "ataque": 48,
        "defensa": 19,
        "tipo": "agua💦"
    }
}

# Tabla de efectividad: (tipo_atacante, tipo_defensor) → multiplicador
efectividad: Dict[Tuple[str, str], float] = {
    ("agua💦", "fuego🔥"): 2.0,
    ("fuego🔥", "agua💦"): 0.5,
    ("eléctrico⚡", "agua💦"): 2.0,
    ("agua💦", "eléctrico⚡"): 0.5,
    ("fuego🔥", "eléctrico⚡"): 1.0,
    ("eléctrico⚡", "fuego🔥"): 1.0,
}


def calcular_daño(atacante: Dict[str, int | str], defensor: Dict[str, int | str]) -> None:
    tipo_atacante: str = atacante["tipo"]
    tipo_defensor: str = defensor["tipo"]
    multiplicador: float = efectividad.get((tipo_atacante, tipo_defensor), 1.0)
    ataque: int = atacante["ataque"]
    defensa: int = defensor["defensa"]
    dano_base: int = ataque - defensa
    dano: int = int(dano_base * multiplicador)
    dano = max(dano, 10)
    vida_actual: int = defensor["vida"]
    vida_actualizada: int = max(vida_actual - dano, 0)
    defensor["vida"] = vida_actualizada
    print(f"{tipo_atacante} ataca a {tipo_defensor}")
    if multiplicador > 1.0:
        print("Es super efectivo")
    elif multiplicador < 1.0:
        print("No es tan efectivo")
    print(f"daño provocado: {dano}")
    print(f"vida restante: {vida_actualizada}")


def combate(p1_name: str, p2_name: str) -> None:
    pokemon1: Dict[str, int | str] = pokemon[p1_name].copy()
    pokemon2: Dict[str, int | str] = pokemon[p2_name].copy()

    print(f"🔥 Combate entre {p1_name} y {p2_name} 🔥\n")

    turno: int = 0
    while pokemon1["vida"] > 0 and pokemon2["vida"] > 0:
        if turno % 2 == 0:
            atacante: Dict[str, int | str] = pokemon1
            defensor: Dict[str, int | str] = pokemon2
            print(f"{p1_name} ataca {p2_name} !\n")
        else:
            atacante = pokemon2
            defensor = pokemon1
            print(f"{p2_name} ataca {p1_name} !\n")

        calcular_daño(atacante, defensor)
        turno += 1

    if pokemon1["vida"] > 0:
        print(f"🏆 ¡{p1_name} gana el combate!\n")

    if pokemon2["vida"] > 0:
        print(f"🏆 ¡{p2_name} gana el combate!\n")


def añadir_pokemon(nombre: str, vida: int, ataque: int, defensa: int, tipo_emoj: str) -> None:
    pokemon[nombre] = {
        "vida": vida,
        "ataque": ataque,
        "defensa": defensa,
        "tipo": tipo_emoj
    }


def añadir_efectividad(tipo_atacante: str, tipo_defensor: str, multiplicador: float) -> None:
    efectividad[(tipo_atacante, tipo_defensor)] = multiplicador


añadir_pokemon("Bulbasaur", 100, 49, 15, "planta🌿")
añadir_efectividad("planta🌿", "agua💦", 2.0)
añadir_efectividad("agua💦", "planta🌿", 0.5)
añadir_efectividad("planta🌿", "fuego🔥", 0.5)
añadir_efectividad("fuego🔥", "planta🌿", 2.0)
añadir_efectividad("planta🌿", "eléctrico⚡", 1.0)
añadir_efectividad("eléctrico⚡", "planta🌿", 1.0)

# combate("Pikachu", "Squirtle")
# combate("Pikachu", "Charmander")
# combate("Squirtle", "Charmander")
# combate("Charmander", "Squirtle")
combate("Charmander", "Bulbasaur")
# combate("Pikachu", "Pikachu")
