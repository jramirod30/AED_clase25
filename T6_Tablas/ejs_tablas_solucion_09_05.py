from typing import List, Dict, Tuple

poblaciones: List[Tuple[str, str]] = [
    ("Toledo", "Juan"),
    ("Madrid", "Pepe"),
    ("Toledo", "Luis"),
    ("Bilbao", "Ana"),
    ("Jaen", "Eva"),
]


def get_max_poblacion(pares: List[Tuple[str, str]]) -> str:
    """
    PRE: pares no está vacío

    POST: devuelve el nombre de la ciudad con más habitantes
    """
    counter:Dict[str, int] = {}
    for poblacion in pares:
        if poblacion[0] in counter:
            counter[poblacion[0]] += 1
        else:
            counter[poblacion[0]] = 1
    max_poblacion:int = 0
    ciudad:str = ""
    for key in counter:
        if counter[key] > max_poblacion:
            max_poblacion = counter[key]
            ciudad = key
    return ciudad



def get_population(pares: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    PRE: pares no está vacío

    POST: devuelve un diccionario con las ciudades como claves y
          listas de personas como valores
    """

    poblacion: Dict[str, List[str]] = {}
    for ciudad, persona in pares:
        if ciudad in poblacion:
            poblacion[ciudad].append(persona)
        else:
            poblacion[ciudad] = [persona]
    return poblacion



