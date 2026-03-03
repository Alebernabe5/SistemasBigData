# Análisis Diagnóstico: Gasto Educativo en España (Actividad 2.2)

Este proyecto aplica técnicas de **Analítica Diagnóstica** para determinar la causa raíz de la variabilidad del gasto público en educación entre las diferentes Comunidades Autónomas de España. Utilizando el lenguaje **R**, se ha modelado la relación entre el volumen de alumnos y el presupuesto total.

## 📂 Contenido de la Entrega
* **`educacion_final.csv`**: Datos en bruto extraídos del INE, procesados para eliminar separadores de miles y estructurados por CCAA.
* **`script_analisis.R`**: Código fuente en R que automatiza la limpieza, el cálculo estadístico y la generación de gráficos.
* **`Informe_Analisis_Educacion.pdf`**: Documento final con la captura del gráfico y la interpretación técnica del modelo.

## 🛠️ Tecnologías y Versiones
* **R versión 4.5.2** (2025-10-31)
* **RStudio** como entorno de desarrollo.
* **Librerías principales**: `tidyverse` (`ggplot2` para visualización y `dplyr` para gestión de datos).

## 📊 Metodología y Resultados
El análisis se centró en una **Regresión Lineal Simple** ($Y = \beta_0 + \beta_1X + \epsilon$) para validar la hipótesis de que el número de alumnos es el principal *driver* del gasto.

### Métricas Obtenidas:
* **Correlación de Pearson**: **0.9715**. Indica una relación lineal positiva casi perfecta.
* **Coeficiente de Determinación ($R^2$):** **0.9438**.
* **P-value:** **3.194e-08**. Confirma que el modelo es estadísticamente significativo.

### Conclusión del Diagnóstico:
El **94,38%** del gasto educativo regional en España está explicado directamente por el número de estudiantes matriculados. El margen restante se atribuye a variables secundarias como la eficiencia administrativa o diferencias en el gasto medio por alumno propias de cada comunidad (analizadas mediante *Drill-down* regional).

## 🚀 Instrucciones de Ejecución
1. Asegurarse de que `educacion_final.csv` y `script_analisis.R` estén en el mismo directorio.
2. Abrir el script en RStudio.
3