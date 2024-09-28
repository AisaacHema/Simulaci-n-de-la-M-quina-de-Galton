import numpy as np
import matplotlib.pyplot as plt

def simular_galton(num_canicas, num_niveles):
    # Crear un arreglo para contar las canicas en cada compartimento
    bins = np.zeros(num_niveles + 1)
    
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            # Decidir caer a la izquierda (0) o a la derecha (1)
            posicion += np.random.choice([0, 1])
        bins[posicion] += 1
    
    return bins

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados)
    plt.xlabel('Compartimentos')
    plt.ylabel('Número de canicas')
    plt.title('Simulación de la Máquina de Galton')
    plt.xticks(range(len(resultados)))
    plt.grid(axis='y')
    plt.show()

# Parámetros
num_canicas = 3000  # Número de canicas
num_niveles = 12    # Número de niveles de obstáculos

# Simulación
resultados = simular_galton(num_canicas, num_niveles)

# Graficar el resultado
graficar_histograma(resultados)
