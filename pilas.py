def programa_pilas():
    ejecutar = True
    while ejecutar:
        pila = []
        while True:
            print("\n--- Menú Pilas ---")
            print("1. Insertar pila")
            print("2. Borrar en pila")
            print("3. Listar pila")
            print("4. Salir")
            
            opcion = input("Elige una opción (1-4): ")
            
            if opcion == '1':
                numero = input("Ingresa un número para apilar: ")
                pila.append(numero)
                print(f"Número {numero} insertado en la pila.")
            elif opcion == '2':
                if len(pila) > 0:
                    eliminado = pila.pop() # Saca el último elemento (LIFO)
                    print(f"Elemento {eliminado} sacado de la pila.")
                else:
                    print("La pila está vacía.")
            elif opcion == '3':
                print(f"Lista completa actual de la pila: {pila}")
            elif opcion == '4':
                print("Saliendo del menú de pilas...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        repetir = input("¿Deseas ejecutar nuevamente el programa de pilas? (s/n): ").lower()
        if repetir != 's':
            ejecutar = False
            print("Programa finalizado.")

# Para ejecutar el programa, llama a la función:
programa_pilas()