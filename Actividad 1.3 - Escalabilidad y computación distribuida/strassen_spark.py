from pyspark import SparkConf, SparkContext
import numpy as np
import time
import os
import sys

# Configurar Spark
os.environ['PYSPARK_PYTHON'] = r"C:\Users\Ale\AppData\Local\Programs\Python\Python313\python.exe"
os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\Ale\AppData\Local\Programs\Python\Python313\python.exe"

conf = SparkConf() \
    .setAppName("StrassenFinal") \
    .setMaster("local[*]") \
    .set("spark.driver.host", "127.0.0.1") \
    .set("spark.driver.bindAddress", "127.0.0.1") \
    .set("spark.python.worker.reuse", "false")
    

sc = SparkContext(conf=conf)
# Desactivamos el servidor de acumuladores problemático en Windows
sc._jsc.sc().setLocalProperty("spark.scheduler.pool", "default")

# --- Algoritmo de Strassen (versión recursiva simple) ---
def strassen(A, B):
    n = len(A)
    if n == 1:
        return A * B
    k = n // 2
    A11, A12, A21, A22 = A[:k,:k], A[:k,k:], A[k:,:k], A[k:,k:]
    B11, B12, B21, B22 = B[:k,:k], B[:k,k:], B[k:,:k], B[k:,k:]

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

# --- Función distribuida ---
def strassen_distributed(data):
    A, B = data
    return strassen(A, B)
# --- Generar matrices aleatorias ---
N = 150
A = np.random.randint(0, 10, (N, N))
B = np.random.randint(0, 10, (N, N))

k = N // 2
submatrices = [
    (A[:k,:k], B[:k,:k]),
    (A[:k,k:], B[k:,:k]),
    (A[k:,:k], B[:k,k:]),
    (A[k:,k:], B[k:,k:])
]

# --- Enviar las tareas al cluster ---
start = time.time()
rdd = sc.parallelize(submatrices, numSlices=4)
partial_results = rdd.map(strassen_distributed).collect()
end = time.time()

# --- Combinar los resultados ---
C_top = np.hstack((partial_results[0], partial_results[1]))
C_bottom = np.hstack((partial_results[2], partial_results[3]))
C = np.vstack((C_top, C_bottom))

print("✅ Multiplicación completada.")
print("⏱️ Tiempo total:", round(end - start, 2), "segundos")

sc.stop()
