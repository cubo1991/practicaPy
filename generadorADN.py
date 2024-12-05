elementosMatriz = ['A', 'G', 'T', 'C']

def bnRandom (n = 6):
    import random
    matriz = []

  
    contador = 0
    while True:
        matriz.append(random.choices(elementosMatriz, k=n))
     
        contador = contador + 1
        if contador == 5:
            break

  

    return matriz


