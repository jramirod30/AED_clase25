from agenda import Agenda
from datos_personales import DatosPersonales

agenda: Agenda = Agenda()

agenda.insertar("p", DatosPersonales(34, "", "a"))
agenda.insertar("p1", DatosPersonales(35, "", "a"))
agenda.insertar("p2", DatosPersonales(34, "", "a"))
agenda.insertar("q", DatosPersonales(34, "", "b"))
agenda.insertar("q2", DatosPersonales(34, "", "b"))
agenda.insertar("r", DatosPersonales(34, "", "c"))

#print(agenda)

print(agenda.get_contactos_igual_direccion())
print(agenda.get_contactos_igual_direccion1())

agenda.borrar("p")

print(agenda)

print(agenda.buscar("p1"))




