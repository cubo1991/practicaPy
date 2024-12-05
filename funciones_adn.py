

def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def mostrarLineasMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    
            