from typing import Dict, Optional, List
from datos_personales import DatosPersonales


class Agenda:
    def __init__(self):
        self.__contactos: Dict[str, DatosPersonales] = {}

    def buscar(self, nombre: str) -> Optional[DatosPersonales]:
        return self.__contactos.get(nombre)

    def insertar(self, nombre: str, info: DatosPersonales) -> None:
        if nombre in self.__contactos:
            raise ValueError("nombre ya existe")
        else:
            self.__contactos[nombre] = info

    def borrar(self, nombre: str) -> None:
        if nombre in self.__contactos:
            self.__contactos.pop(nombre)

    def __str__(self) -> str:
        result: str = ""
        for key in sorted(self.__contactos.keys()):
            result += key + "\t" + str(self.__contactos[key]) + "\n"
        return result

    def get_contactos_igual_direccion(self) -> List[str]:
        direcciones: Dict[str, List[str]] = {}
        for nombre in self.__contactos.keys():
            direccion: str = self.__contactos[nombre].direccion
            if direccion != "":
                if direccion in direcciones:
                    direcciones[direccion] += [nombre]
                else:
                    direcciones[direccion] = [nombre]

        result: List[str] = []
        for nombres in direcciones.values():
            if len(nombres) > 1:
                result += nombres

        return result

    def get_contactos_igual_direccion1(self) -> List[List[str]]:
        direcciones: Dict[str, List[str]] = {}
        for nombre in self.__contactos.keys():
            direccion: str = self.__contactos[nombre].direccion
            if direccion != "":
                if direccion in direcciones:
                    direcciones[direccion] += [nombre]
                else:
                    direcciones[direccion] = [nombre]

        result: List[List[str]] = []
        for nombres in direcciones.values():
            if len(nombres) > 1:
                result += [nombres]

        return result
