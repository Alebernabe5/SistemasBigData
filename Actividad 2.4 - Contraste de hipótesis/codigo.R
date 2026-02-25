#Simulacion de datos
set.seed(123)
muestra_cpus <- rnorm(n = 50, mean =58, sd =5)
#parametros
media_muestral <- mean(muestra_cpus)
mu_teorica <- 60
sigma_conocida <- 5
n <- 50
#calculo de z_score
z_score <- (media_muestral - mu_teorica) / (sigma_conocida / sqrt(n))
print(z_score)
#calculo de p_Valor
p_valor <- 2 * pnorm(-abs(z_score))
print(paste("P-Valor:", p_valor))

#analizando la muestra de los nuevos procesadores, he notado que la temperatura ha bajado unos dos grados. El analisis estatico confirma que esta mejora es real y no del azar. Podemos confirmar que la nueva pasta terminca es mas eficiente y efectiva.

#parte2 el t-test
#simulacion de datos
tiempos_nuevos <- c(28, 29, 30, 25, 27, 29, 31, 24, 26, 29,
                    28, 27, 30, 26, 25, 28, 29, 30, 24, 27)
#planteamiento de partes

#ejecucion del test
resultado_t <- t.test(tiempos_nuevos, mu = 30, alternative = "less")
print(resultado_t)

#La nueva funcionalidad de pedido rapido ha logrado reducir el tiempo de entrega promedio.El test da un error bajo, por lo que la herramienta cumple con su objetivo reduciendo tiempos por debajo de lo habitual.
#comparacion de dos muestras
gasto_android <- rnorm(30, mean=15, sd=5)
gasto_ios <- rnorm(30, mean=18, sd=5) # Simulamos que gastan más


# Test Bilateral (two.sided)
t.test(gasto_android, gasto_ios, alternative = "two.sided", var.equal = FALSE)

#chi-cuadrado
#creacion de la tabla de contigencia
# Filas: Compró / No Compró
# Columnas: Campaña A / Campaña B
datos_campana <- matrix(c(30, 70,   # Campaña A: 30 compran, 70 no
                          50, 50),  # Campaña B: 50 compran, 50 no
                        nrow = 2,
                        byrow = FALSE)


colnames(datos_campana) <- c("Campaña_A", "Campaña_B")
rownames(datos_campana) <- c("Compró", "No_Compró")
print(datos_campana)

#planteamiento y ejecucion del test
test_chi <- chisq.test(datos_campana)
print(test_chi)
#Comparaando el comportamiento de compra, vemos que los de IOS gastan en promedio mas que los de android. Veo que la diferencia de consumo es ignificativa entre ambas platafotmas.
