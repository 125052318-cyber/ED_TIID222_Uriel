def programa_colas():
    ejecutar = True
    while ejecutar:
        cola = []
        while True:
            print("\n--- Menú Colas ---")
            print("1. Insertar cola")
            print("2. Borrar en cola")
            print("3. Listar cola")
            print("4. Salir")
            
            opcion = input("Elige una opción (1-4): ")
            
            if opcion == '1':
                numero = input("Ingresa un número para encolar: ")
                cola.append(numero)
                print(f"Número {numero} insertado en la cola.")
            elif opcion == '2':
                if len(cola) > 0:
                    eliminado = cola.pop(0) # Saca el primer elemento (FIFO)
                    print(f"Elemento {eliminado} sacado de la cola.")
                else:
                    print("La cola está vacía.")
            elif opcion == '3':
                print(f"Lista completa actual de la cola: {cola}")
            elif opcion == '4':
                print("Saliendo del menú de colas...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        repetir = input("¿Deseas ejecutar nuevamente el programa de colas? (s/n): ").lower()
        if repetir != 's':
            ejecutar = False
            print("Programa finalizado.")

# Para ejecutar el programa, llama a la función:
programa_colas()