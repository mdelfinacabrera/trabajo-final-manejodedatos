# **Trabajo Final - Manejo de Datos en Biología Computacional. Herramientas de Estadística**
## ***Estudiante: María Delfina Cabrera***

Este repositorio contiene el análisis estadístico realizado para el trabajo final de la Especialización en Bioinformática. 

## Marco Teórico
La simbiosis rizobio-leguminosa permite fijar nitrógeno atmosférico de forma natural, reemplazando fertilizantes químicos y beneficiando la agricultura sustentable. Sin embargo, la liberación masiva de rizobios como inoculantes puede afectar la microbiota nativa del suelo, en parte por la transferencia horizontal de genes (HGT). La conjugación bacteriana es uno de los mecanismos más eficientes de HGT y juega un rol clave en la evolución de estas bacterias.
En el plásmido pLPU83a de *Rhizobium favelukesii* LPU83, nuestro laboratorio identificó dos genes conservados (*rcgR* y *rcgA*) implicados en la transferencia conjugativa de plásmidos. Mi trabajo de tesis busca caracterizar su función y relevancia en la regulación de la transferencia conjugativa, aportando al entendimiento de los mecanismos moleculares que gobiernan la propagación génica en rizobios. 
Contamos con evidencia que demuestra que *rcgR* reprime la transferencia conjugativa. Es por esto que realizamos transcriptómica (cuyos resultados parecen alinearse con nuestra hipótesis) y proteómica sobre la cepa wild-type y su mutante en dicho gen. Los datos proteómicos no fueron analizados aún en profundidad, por lo que elegí utilizarlos para este trabajo.

## Obtención de los datos utilizados en este trabajo
Para obtener las tablas de datos proteómicos, primero se aislaron las proteínas. Para esto, se separaron las células del medio de cultivo, obteniendo un pellet celular el cual fue resuspendido en un buffer adecuado para la solubilización de proteínas y compatible con la digestión con tripsina. Luego se desnaturalizaron las proteínas para exponer sus residuos internos y se redujeron los enlaces disulfuro, rompiendo estructuras terciarias/cuaternarias. A continuación se las incubó en condiciones que favorecerieron la desnaturalización completa de las proteínas y la reducción de enlaces disulfuro, y se alquiló para bloquear los grupos sulfhidrilo libres, evitando que se reformen enlaces disulfuro. Luego se ajustaron condiciones para la digestión con tripsina y en el siguiente paso se procedió a digerir con dicha enzima. Se purificaron los peptidos y se lavaron para eliminar residuos no deseados. Posteriormente se secaron al vacío para remover el solvente y concentrar la muestra, se midieron en nanodrop y se separaron e identificaron por LC-MS/MS. Esto se repitió por triplicado para cada condición.
La tabla cruda de datos fue anotada con DIA-NN, y la nueva tabla con las anotaciones es la utilizada en este trabajo.

El dataset cotiene una tabla con las siguientes columnas:
➤ Protein.Group: Identificador interno del grupo de proteínas.
➤ Protein.Ids: Lista de identificadores únicos. Puede contener múltiples IDs si hay ambigüedad.
➤ Protein.Names: Nombres de las proteínas correspondientes a los IDs anteriores.
➤ Genes: Nombres de los genes codificantes de las proteínas detectadas. 
➤ First.Protein.Description: Descripción funcional de la primera proteína listada en el grupo. Incluye información como función putativa, localización, o familia proteica.
➤ WT-1, WT-2 y WT-3: Valores de la abundancia proteíca relativa en las tres réplicas biológicas de *Rhizobium favelukesii* LPU83 wild-type.
➤ MUT-1, MUT-2 y MUT-3: Valores de la abundancia proteíca relativa en las tres réplicas biológicas de *Rhizobium favelukesii* LPU83 mutante en *rcgR*.
Dicho dataset se puede visualizar en `datos_proteomica.csv`

## Objetivo
Con un avistaje general de los datos proteómicos, y más puntualmente en las proteínas conjugativas del plásmido pLPU83a, se observó que la mayoría de ellas están ausentes en la cepa wild-type y presentes en la cepa mutante, lo cual concuerda con los resultados previos del laboratorio. Sin embargo, también resulta de interés evaluar si la eliminación del gen *rcgR* afecta la expresión de otras proteínas no relacionadas directamente con la transferencia conjugativa.
Es por esto que como objetivo de este trabajo planteé comparar las proteínas obtenidas tanto para *Rhizobium favelukesii* LPU83 wild-type (WT) como para *Rhizobium favelukesii* LPU83 mutante en *rcgR* (MUT)

## Hipótesis
La deleción de *rcgR* no induce alteraciones globales en la expresión proteica, sino que su efecto regulador se limita a un subconjunto específico de genes.

# Paso a paso
***Variable***
Variable evaluada: Abundancia relativa de proteínas (por muestra y proteína)
Tipo: Continua

***Importar y filtrar los datos***
Importar el dataset original, transformarlo en valores de logaritmo en base 2 y filtrar los NaN. De esta manera, solo me quedan filas sin NaN, por lo que me quedo únicamente con proteínas expresadas en ambas condiciones.

***Descripción y distribución de los datos***
Primero utilicé .describe para poder observar la descripción de los datos. A partir de esto, pude observar:
- Número de datos (count): En todas las réplicas hay 3549 proteínas cuantificadas (sin datos faltantes).
- Media (mean): Las medias son muy similares entre réplicas y condiciones: alrededor de 18.5. Esto indica que, en promedio, la abundancia proteica total no varía mucho entre WT y MUT.
- Desviación estándar (std): La variabilidad dentro de cada réplica es parecida (~2.3 - 2.4), lo que indica dispersión similar en la intensidad de proteínas en ambas condiciones.
- Mínimo (min): Los valores mínimos son bastante bajos (~10-11 log2), sugiriendo algunas proteínas con baja expresión o detección límite.
- Cuartiles (25%, 50%, 75%):
  El primer cuartil (25%) está alrededor de 16.8-16.9.
  El segundo cuartil (50%) está alrededor de 18.4. Esto 
  El tercer cuartil (75%) está en torno a 20.05-20.08.
- Máximo (max): Valores máximos altos (~29), lo que indica proteínas con alta abundancia detectadas.
Si se observa la media y el segundo cuartil para cada réplica, la media es consistentemente ligeramente superior a la mediana (~0.1), lo cual sugiere una leve asimetría a la derecha.

Luego, realicé un histograma para cada columna.
Los histogramas pueden observarse en las imágenes adjuntas:
- 'histograma_wt_1.png'
- 'histograma_wt_2.png'
- 'histograma_wt_3.png'
- 'histograma_mut_1.png'
- 'histograma_mut_2.png'
- 'histograma_mut_3.png'
A simple vista, esos histogramas parecerían seguir una ditribución normal. Si los miramos con detenimiento, podemos observar la campana un poco corrida a la izquierda y que las colas son chatas pareciendo ser la derecha más abacrativa que la izquierda. Esto se alinea con la observación de la media y la mediana descripta anteriormente, sugiriendo una leve asimetría a la derecha. Es por esto que el siguiente paso fue la evaluación de asimetría.

***Evaluación de asimetría y curtosis***
Para esto, se analizó la asimetria y curtosis de la distribucion de los datos de cada réplica, calculando el coeficiente de asimetria de Fisher y el coeficiente de curtosis.
Todos los valores de los coeficientes de asimetría son positivos y están cerca de 0.3, indicando una ligera asimetría positiva (cola derecha más larga), lo que coincide con lo observado anteriormente.
Por otro lado, los coeficientes de curtosis están muy cerca de 0 (entre 0.06 y 0.14), lo que indica distribuciones ligeramente leptocúrticas respecto a la normal, pero sin ser extremo.

***Intervalos de confianza***
Para estimar los intervalos de confianza de los datos para cada muestra, asumi distribucion normal dado que el n>30. En este caso, calcule los intervalos de confianza definiendo los siguientes parametros:
- confidence = 95% = 0.95
- loc = media 
- scale= desviacion estandar
Los resultados fueron:
log2_WT-1: Media=18.573, IC 95% normal = [18.495, 18.651]
log2_WT-2: Media=18.542, IC 95% normal = [18.463, 18.620]
log2_WT-3: Media=18.514, IC 95% normal = [18.434, 18.593]
log2_MUT-1: Media=18.505, IC 95% normal = [18.426, 18.585]
log2_MUT-2: Media=18.534, IC 95% normal = [18.455, 18.613]
log2_MUT-3: Media=18.518, IC 95% normal = [18.439, 18.598]
Los intervalos de confianza del 95% para cada réplica indican una gran consistencia interna y una alta superposición entre las condiciones wild-type y mutante. Esto sugiere que la eliminación del gen *rcgR* no produce una alteración global en los niveles de abundancia proteica.

***Verificación de supuestos***
*Supuesto de normalidad. Test de normalidad*
Para verificar si los datos se distribuyen normalmente, se realizo un test de normalidad (Normal test). Para esto, se plantearon las siguientes dos hipótesis:
H0: los datos se distribuyen normalmente.
H1: los datos no se distribuyen normalmente.
En todos los casos, el pvalue es menor a 0.05, por lo que se rechaza la hipótesis nula de normalidad; los datos no se distribuyen de manera normal.

*Supuesto de homocedasticidad de varianzas. Test de Levene*
Para verificar similitud de varianzas, se realizó un test de Levene. Se plantearon dos hipotesis:
H0 = homocedasticidad de varianzas en la abundancia relativa de proteínas de las muestras es debido al azar.
H1 = homocedasticidad de varianzas en la abundancia relativa de proteínas de las muestras no es debido al azar.
El pvalor es mayor a 0.05, por lo que no se rechaza la hipótesis nula y se puede asumir homocedasticidad de varianzas.

De todas formas, como en el test de normalidad tuve que rechazar la hipótesis nula, tengo que hacer un test no parametrico para comparar los grupos. Sin embargo, dado que este test puede detectar pequeñas desviaciones de normalidad como estadísticamente significativas, decidí evaluar los datos tanto como paramétricos (que es lo que se suele utilizar en análisis proteómicos) como como no paramétricos.

***Tests estadísticos***
*Test no paramétrico: prueba de Mann-Whitney*
Con el objetivo de comparar si la abundancia relativa total de las proteínas entre la cepa wild-type y la sepa mutante presentaba diferencias estadísticamente significativas, realicé la prueba de Mann-Whitney.
Como el pvalor fue mayor a 0.05 (p-value = 0.4026), este test estadístico nos indica que no hay diferencias significativas entre wild type y mutante.

Como el objetivo de una proteómica es, además, comparar la abundancia relativa de cada proteína tanto en la cepa wild-type como la cepa mutante, utilicé tanto el método no paramétrico (prueba de Mann-Whitney) como el método paramétrico (t-test) para evaluar la significancia en cada fila. Para el método paramétrico sumé el parámetro de magnitud de cambio (FoldChange), ya que no solamente alcanza con el p-value para asumir una diferencia entre la abundancia proteica relativa.
Estos resultados se pueden ver en las tablas
- 'resultado_mannwhitney_proteina.csv': resultados de la prueba de Mann Whitney proteína por proteína
- 'resultado_ttest_fc_proteina.csv': resultados del t-test con fold-change proteína por proteína
Por un lado, con la prueba de Mann Whitney no se observaron p-valores menores a 0.05, lo que estaría indicando que no hay proteínas con diferencias en su expresión entre ambas condiciones.
Respecto al t-test, para decir que las proteínas están diferencialmente expresadas se utilizó como corte que el p-valor debe ser menor a 0.05 y el |log2FoldChange| debe ser mayor a |2|. Utilizando este criterio, no se observaron proteínas diferencialmente expresadas entre ambas condiciones.
Se agregó en el código que se impriman las 10 proteínas con menor p-valor porque me pareció que da un paneo rápido de lo que después se va a observar en la tabla completa.
Además, en el t-test también se guardó un archivo con las proteínas cuyo p-valor es menor a 0.05 y cuyo |log2FoldChange| es mayor a |2|. En este caso, el archivo quedó vacío, razón por la cual no se encuentra adjunto.

Los resultados coinciden con el test no paramétrico de que no existen proteínas sobre o subexpresadas.


## Conclusiones
A través del análisis estadístico tanto de manera global como proteína por proteína, utilizando pruebas no paramétricas (Mann Whitney) y paramétricas (t-test), no se detectaron cambios significativos en la abundancia relativa de proteínas entre las condiciones analizadas.
Estos resultados sugieren que el efecto del gen *rcgR* se limita principalmente al sistema conjugativo, sin generar alteraciones globales en el perfil proteico de la cepa. En consecuencia, se refuerza la idea de que esta proteína hipotética actúa como un regulador focalizado sobre genes específicos del plásmido pLPU83a, sin impactar de manera general sobre la fisiología celular.

## Perspectivas para lo aprendido en esta materia
Si bien no pude hacer la materia de manera sincrónica, me ayudó mucho a entender un poco más de estadística y no caer siempre en el t-test.
Quisiera aplicar este análisis a otros datos proteómicos y, a futuro, también me va a servir cuando tenga que analizar estadística de peso seco de plantas. Además, tengo pensado como próximo desafío intentar transformar mis tablas de proteómica en un binomio para poder observar presencia-ausencia de manera más analítica y no solo solo visualmente. Es una herramienta que me va a facilitar el avistaje de datos que por el momento vengo haciendo de forma manual. Voy a utilizar como base lo que vimos respecto a distribuciones binomiales en la materia. Sin embargo, no lo elegí como tema para mi trabajo final porque me pareció más representativo de los conceptos aprendidos utilizar una distribución que, en un principio, creí iba a comportarse como distribución normal.
