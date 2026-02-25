import requests
import pandas as pd
from datetime import datetime

# URL API
url = "https://servicios.ine.es/wstempus/jsCache/ES/DATOS_TABLA/25171"

print("Consultando API del INE...")
response = requests.get(url)
data = response.json()

# Filtrar información
# General e Indice
datos_filtrados = []

for serie in data:
    nombre_serie = serie['Nombre']
    
    # Aplicamos el filtro 
    if "Índice" in nombre_serie and "General" in nombre_serie:
        
        # Separacion de datos
        partes = nombre_serie.split('.')
        lugar = partes[2].strip() if len(partes) > 2 else "Total Nacional"
        
        for obs in serie['Data']:
            # Transformacion a la estructura solicitad
            registro = {
                "Lugar": lugar,
                "Año": obs['Anyo'],
                "Periodo": obs['FK_Periodo'],
                "IPV": obs['Valor']
            }
            datos_filtrados.append(registro)

# Dataframe
df = pd.DataFrame(datos_filtrados)

# Guardado local con la fecha de hoy
fecha_peticion = datetime.now().strftime("%d_%m_%Y")
nombre_archivo = f"IPV_{fecha_peticion}.csv"

df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')

print("-" * 30)
print(f"Filtros aplicados: 'General' e 'Índice'")
print(f"Archivo guardado: {nombre_archivo}")
print(f"Número de registros: {len(df)}")
print("-" * 30)