
if (!require("jsonlite")) install.packages("jsonlite")
if (!require("dplyr")) install.packages("dplyr")
library(jsonlite)
library(dplyr)

#  Cargar los datos
datos_crudos <- fromJSON("datos.json")

# Extraemos los datos y los nombres de las series
df_list <- lapply(1:nrow(datos_crudos), function(i) {
  df_temp <- datos_crudos$Data[[i]]
  df_temp$Serie_Nombre <- datos_crudos$Nombre[i]
  return(df_temp)
})
datos_ipc_completo <- bind_rows(df_list)

# Limpiar y Subconjuntos
# Filtramos de forma muy flexible para evitar errores de tildes o puntos
datos_indices <- datos_ipc_completo %>% 
  # Buscamos  la palabra "indice" pero NO "Variación"
  filter(grepl("Índice", Serie_Nombre) & !grepl("Variación", Serie_Nombre)) %>%
  mutate(Valor = as.numeric(Valor))

# Creamos los subconjuntos por palabras clave 
general <- datos_indices %>% filter(grepl("general", Serie_Nombre, ignore.case = TRUE))
vivienda <- datos_indices %>% filter(grepl("Vivienda", Serie_Nombre, ignore.case = TRUE))


# Estadísticas sobre el IPC General por año
analisis_general_anual <- general %>%
  group_by(Anyo) %>%
  summarise(
    Media = mean(Valor, na.rm = TRUE),
    Mediana = median(Valor, na.rm = TRUE),
    Desv_Tipica = sd(Valor, na.rm = TRUE),
    Maximo = max(Valor, na.rm = TRUE),
    Minimo = min(Valor, na.rm = TRUE)
  )

print("--- ANÁLISIS GENERAL POR AÑO ---")
print(analisis_general_anual)

# Desviación típica por serie encontrada
desv_por_producto <- datos_indices %>%
  group_by(Serie_Nombre) %>%
  summarise(Desv_Tipica_Total = sd(Valor, na.rm = TRUE))

print("--- DESVIACIÓN POR SERIE ---")
print(desv_por_producto)

# Representación
# Dibujamos solo si hemos encontrado datos 
if(nrow(general) > 0) {
  # Ordenar por fecha cronológicamente
  general_plot <- general %>% arrange(Fecha)
  
  plot(general_plot$Valor, type="o", col="blue", pch=16,
       main="Evolución IPC: Índice General", 
       ylab="Índice", xlab="Meses acumulados")
  
  if(nrow(vivienda) > 0) {
    vivienda_plot <- vivienda %>% arrange(Fecha)
    lines(vivienda_plot$Valor, col="red", type="o", pch=17)
    legend("topleft", legend=c("General", "Vivienda"), 
           col=c("blue", "red"), lty=1, pch=16:17, bty="n")
  }
} else {
  print("ADVERTENCIA: No se han encontrado datos para graficar. Revisa los filtros.")
}

#  Exportacion
write.csv(analisis_general_anual, "resumen_ipc_general.csv", row.names = FALSE)