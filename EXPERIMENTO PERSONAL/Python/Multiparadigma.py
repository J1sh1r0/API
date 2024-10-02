def rotate_snake(matrix):
    indices = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
    values = [matrix[x][y] for x, y in indices]
    last = values.pop()
    values.insert(0, last)
    
    for (x, y), value in zip(indices, values):
        matrix[x][y] = value
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriz de ejemplo
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

continuar = 'si'

while continuar.lower() == 'si':
    print("Matriz antes de rotar:")
    print_matrix(matrix)
    
    # Llamamos a la función de rotación
    rotated_matrix = rotate_snake(matrix)
    
    print("\nMatriz después de rotar:")
    print_matrix(rotated_matrix)
    
    continuar = input("\n¿Quieres rotar otra vez? (si/no): ")

print("Fin del programa")
