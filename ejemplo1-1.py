
class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        # Al comenzar, la lista está vacía
        self.head = None


    def insertar(self, dato):

        # Creamos un nuevo nodo
        nuevo_nodo = Nodo(dato)

        # Si la lista está vacía
        if self.head is None:

            # El nuevo nodo será el primero
            self.head = nuevo_nodo

        else:

            # Comenzamos desde el primer nodo
            actual = self.head

            # Buscamos el último nodo
            while actual.siguiente is not None:
                actual = actual.siguiente

            # Conectamos el último nodo con el nuevo
            actual.siguiente = nuevo_nodo

        print(f"\nEl dato {dato} fue insertado correctamente.")

    def mostrar(self):

        # Comprobamos si la lista está vacía
        if self.head is None:
            print("\nLa lista está vacía.")
            return

        # Comenzamos desde el primer nodo
        actual = self.head

        print("\nLista enlazada:")

        # Recorremos todos los nodos
        while actual is not None:

            print(actual.dato, end=" → ")

            # Avanzamos al siguiente nodo
            actual = actual.siguiente

        print("None")


    def buscar(self, dato):

        actual = self.head

        # Recorremos la lista
        while actual is not None:

            # Comparamos el dato
            if actual.dato == dato:

                print(f"\nEl dato {dato} sí existe en la lista.")
                return

            # Avanzamos
            actual = actual.siguiente

        # Si llegamos aquí, no encontramos el dato
        print(f"\nEl dato {dato} no existe en la lista.")


    def eliminar(self, dato):

        # Si la lista está vacía
        if self.head is None:

            print("\nLa lista está vacía.")
            return


        # Si el dato está en el primer nodo
        if self.head.dato == dato:

            # Movemos head al siguiente nodo
            self.head = self.head.siguiente

            print(f"\nEl dato {dato} fue eliminado.")
            return


        # Comenzamos desde el primer nodo
        actual = self.head

        # Buscamos el nodo anterior al que queremos eliminar
        while actual.siguiente is not None:

            # Comprobamos el siguiente nodo
            if actual.siguiente.dato == dato:

                # Saltamos el nodo que queremos eliminar
                actual.siguiente = actual.siguiente.siguiente

                print(f"\nEl dato {dato} fue eliminado.")
                return

            # Avanzamos al siguiente nodo
            actual = actual.siguiente


        # Si no encontramos el dato
        print(f"\nEl dato {dato} no existe en la lista.")


# Creamos nuestra lista enlazada
lista = ListaEnlazada()


while True:

    print("\n================================")
    print("       LISTA ENLAZADA")
    print("================================")
    print("1. Insertar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Eliminar")
    print("5. Salir")
    print("================================")

    # Pedimos al usuario una opción
    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        dato = int(input("Ingresa el dato que deseas insertar: "))

        lista.insertar(dato)


    elif opcion == "2":

        lista.mostrar()


    elif opcion == "3":

        dato = int(input("Ingresa el dato que deseas buscar: "))

        lista.buscar(dato)


    elif opcion == "4":

        dato = int(input("Ingresa el dato que deseas eliminar: "))

        lista.eliminar(dato)

    elif opcion == "5":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpción no válida. Intenta nuevamente.")