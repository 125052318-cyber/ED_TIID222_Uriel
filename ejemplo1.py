""" tema de exposicion: LISTAS ENLAZADAS """

"CREAMOS EL NODO"
class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None

"HACEMOS EL NODO"
nodo1 = nodo(10)
nodo2 = nodo(20)
nodo3 = nodo(30)

nodo1.next = nodo2
nodo2.next = nodo3

"HACEMOS EL ENCABEZADO"
head = nodo1
actual = head

"MOSTRAMOS LA INFORMACIÓN"
while actual is not None:
    print(actual.dato)
    actual = actual.next

