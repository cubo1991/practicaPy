from generadorADN import bnRandom 
from funciones_adn import mostrarMatriz, mostrarLineasMatriz

def main():
 
    nuevaMatriz = bnRandom(6)

    mostrarMatriz(nuevaMatriz)
    mostrarLineasMatriz(nuevaMatriz)

if __name__ == "__main__":
    main()
