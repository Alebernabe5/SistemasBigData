# Análisis y Predicción de Series Temporales: Netflix (NFLX) 📈

Este repositorio contiene un estudio estadístico completo sobre el comportamiento bursátil de Netflix Inc. (NFLX). Se utiliza el modelo **ARIMA** (AutoRegressive Integrated Moving Average) para analizar datos históricos y generar proyecciones de precio a corto plazo.

## 📋 Resumen de Datos
* **Dataset:** 5,959 registros diarios de precios de cierre.
* **Rango Temporal:** Desde el inicio de cotización hasta principios de 2025.
* **Frecuencia:** Anualizada a 252 días bursátiles.

## 🛠️ Requisitos Técnicos
Para ejecutar este análisis, necesitas tener instalado **R** y las siguientes librerías:
```r
install.packages(c("tidyverse", "forecast", "tseries", "lubridate"))