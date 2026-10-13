matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

matriz.append([39, 22, 69, 17])

print("Matriz completa:")
print(matriz)

print("\nFila en el índice 1:")
print(matriz[1])

for indice_fila, fila in enumerate(matriz):
    if 18 in fila:
        print(f"\n18 encontrado en la fila {indice_fila}")
        break

for fila in matriz:
    for numero in fila:
        if numero == 3:
            print(f"3 encontrado en {fila}")
            break