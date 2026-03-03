# --- ACTIVIDAD 2.2: ANÁLISIS DIAGNÓSTICO ---
library(tidyverse)

# 1. Carga de datos 
datos <- read.csv("educacion_final.csv", sep = ",", check.names = FALSE)

# 2. Renombrar columnas para evitar errores 
colnames(datos) <- c("CCAA", "Gasto", "Medio", "Alumnos")

# 3. Analisis de Correlación (Pearson)
valor_cor <- cor(datos$Gasto, datos$Alumnos)
print(paste("Correlación de Pearson:", round(valor_cor, 4)))

# 4. Modelo de Regresión Lineal 
modelo_final <- lm(Gasto ~ Alumnos, data = datos)
summary(modelo_final)

# 5. Drill-down por CCAA
ggplot(datos, aes(x = Alumnos, y = Gasto)) +
  geom_smooth(method = "lm", color = "red", linetype = "dashed", se = FALSE) +
  geom_point(color = "darkblue", size = 3) +
  geom_text(aes(label = CCAA), vjust = -1, size = 3) + 
  labs(title = "Análisis Diagnóstico: Influencia de la Demografía en el Gasto",
       subtitle = "Relación entre número de alumnos y presupuesto total por CCAA",
       x = "Número de Estudiantes",
       y = "Gasto Total en Educación (€)") +
  theme_minimal()
