# ------------------------------------------------------------
# Parte 2: Pruebas de tiempo de ejecución
# ------------------------------------------------------------
import random
import timeit

from practica_complejidad_1 import funcion_alpha, funcion_beta, funcion_delta, funcion_epsilon, funcion_gamma, funcion_omega, funcion_theta, funcion_zeta


if __name__ == "__main__":
    tamanos = [100, 1000, 5000]
    #tamanos = [50000, 100000, 150000]
    
    for n in tamanos:
        lista = [random.randint(1, 100) for _ in range(n)] 
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(10)]  
        estructura = [[[random.randint(1, 100) for _ in range(10)] for _ in range(n)] for _ in range(10)]  
        
        print(f"\nTamaño n = {n}") 
        #print("funcion_gamma:", timeit.timeit(lambda: funcion_gamma(lista), number=1000)) 
        # print("funcion_epsilon:", timeit.timeit(lambda: funcion_epsilon(lista), number=100)) 
        # print("funcion_zeta:", timeit.timeit(lambda: funcion_zeta(matriz), number=10)) 
        #print("funcion_alpha:", timeit.timeit(lambda: funcion_alpha(lista), number=10)) 
        #print("funcion_omega:", timeit.timeit(lambda: funcion_omega(sorted(lista), random.choice(lista)), number=1000))
        #print("funcion_delta:", timeit.timeit(lambda: funcion_delta(estructura), number=10)) 
    
        # Ejemplos controlados para las de mayor complejidad
        #print("funcion_beta (n=10):", timeit.timeit(lambda: funcion_beta(25), number=1)) 
        print("funcion_theta (n=6):", timeit.timeit(lambda: funcion_theta(11), number=1))  