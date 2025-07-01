# Trabajo Final - Manejo de Datos en Biología Computacional. Herramientas de Estadística
### María Delfina Cabrera

Este repositorio contiene el análisis estadístico realizado para el trabajo final de la Especialización en Bioinformática. 

## Breve introducción
La simbiosis rizobio-leguminosa permite fijar nitrógeno atmosférico de forma natural, reemplazando fertilizantes químicos y beneficiando la agricultura sustentable. Sin embargo, la liberación masiva de rizobios como inoculantes puede afectar la microbiota nativa del suelo, en parte por la transferencia horizontal de genes (HGT). La conjugación bacteriana es uno de los mecanismos más eficientes de HGT y juega un rol clave en la evolución de estas bacterias.
En el plásmido pLPU83a de *Rhizobium favelukesii* LPU83, nuestro laboratorio identificó dos genes conservados (*rcgR* y *rcgA*) implicados en la transferencia conjugativa de plásmidos. Mi trabajo de tesis busca caracterizar su función y relevancia en la regulación de la transferencia conjugativa, aportando al entendimiento de los mecanismos moleculares que gobiernan la propagación génica en rizobios. 
Contamos con evidencia que demuestra que *rcgR* reprime la transferencia conjugativa. Es por esto que realizamos transcriptómica (cuyos resultados parecen alinearse con nuestra hipótesis) y proteómica sobre la cepa wild-type y su mutante en dicho gen. Los datos proteómicos no fueron analizados aún en profundidad, por lo que elegí utilizarlos para este trabajo.

## Objetivo
Con un avistaje general de los datos proteómicos, y más puntualmente en las proteínas conjugativas del plásmido pLPU83a, se observó que la mayoría de ellas están ausentes en la cepa wild-type y presentes en la cepa mutante, lo cual concuerda con los resultados previos del laboratorio. Sin embargo, también resulta de interés evaluar si la eliminación del gen *rcgR* afecta la expresión de otras proteínas no relacionadas directamente con la transferencia conjugativa.
Es por esto que como objetivo de este trabajo planteé comparar las proteínas obtenidas para *Rhizobium favelukesii* LPU83 wild-type (WT) y *Rhizobium favelukesii* LPU83 mutante en *rcgR* (MUT)

## Hipótesis
La deleción de *rcgR* no induce alteraciones globales en la expresión proteica, sino que su efecto regulador se limita a un subconjunto específico de genes.

## Archivos
En relación a este trabajo, dejé adjuntos 4 archivos:
- `datos_proteomica.csv`: archivo con datos de entrada 
- `codigo_trabajo.py`: script con el análisis completo
- `resultado_mannwhitney_proteina.csv`: resultados de la prueba Mann Whitney proteína por proteína
- `resultado_ttest_fc_proteina.csv`: resultados del t-test con fold-change proteína por proteína

## Conclusiones
A través del análisis estadístico proteína por proteína, utilizando pruebas no paramétricas (Mann-Whitney) y paramétricas (t-test), no se detectaron cambios significativos en la abundancia relativa de proteínas entre las condiciones analizadas bajo criterios estrictos de significancia estadística (p < 0.05) y magnitud de cambio (|log₂FC| > 2).
Estos resultados sugieren que el efecto del gen *rcgR* se limita principalmente al sistema conjugativo, sin generar alteraciones globales en el perfil proteico de la cepa. En consecuencia, se refuerza la idea de que esta proteína hipotética actúa como un regulador focalizado sobre genes específicos del plásmido pLPU83a, sin impactar de manera general sobre la fisiología celular.

## Perspectivas para lo aprendido en esta materia
Si bien no pude hacer la materia de manera sincrónica, me ayudó mucho a entender un poco más de estadística y no caer siempre en el t-test.
Quisiera aplicar este análisis a otros datos proteómicos y, a futuro, también me va a servir cuando tenga que analizar estadística de peso seco de plantas. Además, tengo pensado como próximo desafío intentar transformar mis tablas de proteómica en un binomio para poder observar presencia-ausencia de manera más analítica y no solo solo visualmente. Es una herramienta que me va a facilitar el avistaje de datos que por el momento vengo haciendo de forma manual. Voy a utilizar como base lo que vimos respecto a distribuciones binomiales en la materia. Sin embargo, no lo elegí como tema para mi trabajo final porque me pareció más representativo de los conceptos aprendidos utilizar una distribución que, en un principio, creí iba a comportarse como distribución normal.
