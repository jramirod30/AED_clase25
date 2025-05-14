

class DatosPersonales:
    def __init__(self, movil: int, email: str = "", direccion: str = ""):
        self.__movil = movil
        self.__email = email
        self.__direccion = direccion

    @property
    def movil(self) -> int:
        return self.__movil

    @property
    def email(self) -> str:
        return self.__email

    @property
    def direccion(self) -> str:
        return self.__direccion

    @movil.setter
    def movil(self, new: int) -> None:
        self.__movil = new

    @email.setter
    def email(self, new: str) -> None:
        self.__email = new

    @direccion.setter
    def direccion(self, new: str) -> None:
        self.__direccion = new

    def __str__(self) -> str:
        return str(self.movil) + " " + self.email + " " + self.direccion
