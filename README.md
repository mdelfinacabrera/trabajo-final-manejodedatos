# Trabajo Final - Manejo de Datos en Biología Computacional. Herramientas de Estadística
María Delfina Cabrera

Este repositorio contiene el análisis estadístico realizado para el trabajo final de la Especialización en Bioinformática. 

## Breve introducción
La simbiosis rizobio-leguminosa permite fijar nitrógeno atmosférico de forma natural, reemplazando fertilizantes químicos y beneficiando la agricultura sustentable. Sin embargo, la liberación masiva de rizobios como inoculantes puede afectar la microbiota nativa del suelo, en parte por la transferencia horizontal de genes (HGT). La conjugación bacteriana es uno de los mecanismos más eficientes de HGT y juega un rol clave en la evolución de estas bacterias.
En el plásmido pLPU83a de Rhizobium favelukesii LPU83, nuestro laboratorio identificó dos genes conservados (LPU83a_0146 y LPU83a_0148) implicados en la transferencia conjugativa de plásmidos. Mi trabajo de tesis busca caracterizar su función y relevancia en la regulación de la TC, aportando al entendimiento de los mecanismos moleculares que gobiernan la propagación génica en rizobios. 
Contamos con evidencia que demuestra que LPU83a_0146 reprime la transferencia conjugativa. Es por esto que realizamos transcriptómica (cuyos resultados parecen alinearse con nuestra hipótesis) y proteómica. Los datos proteómicos no fueron analizados aún en profundidad, por lo que elegí utilizarlos para este trabajo.

## Objetivo
Comparar las proteínas obtenidas para Rhizobium favelukesii LPU83 wild-type (WT) y Rhizobium favelukesii LPU83 mutante en LPU83a_0146 (MUT)

### Pregunta a responder
Con un avistaje general de los datos proteómicos, y más puntualmente en las proteínas conjugativas del plásmido pLPU83a, ya pude observar que ya mayoría de ellas están ausentes en la cepa wild-type y presentes en la cepa mutante. Sin embargo, también me interesa observar qué sucede con el resto de las proteínas.
- ¿Son únicamente las proteínas conjugativas del plásmido pLPU83a las afectadas, o esta proteína hipotética también se encarga de regular otras proteínas?

## Archivos
En relación a este trabajo, dejé adjuntos 4 archivos:
- `datos_proteomica.csv`: archivo con datos de entrada 
- `codigo_trabajo.py`: script con el análisis completo
- `resultado_mannwhitney_proteina.csv`: resultados de la prueba Mann Whitney proteína por proteína
- `resultado_ttest_fc_proteina.csv`: resultados del t-test con fold-change proteína por proteína

