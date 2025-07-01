# CÓDIGO - TRABAJO FINAL

# Importar las librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import statsmodels.api as sm
import statsmodels.stats.power as smp

# Importar Dataset
path = r'c:\Users\maria\OneDrive\Documentos\Doctorado\Cursos\Especialización en Bioinformática\Segundo año\Manejo de Datos en Biología Computacional. Herramientas de Estadística\datos_proteomica.csv'
datos_prot = pd.read_csv(path)

# Ver las primeras 5 filas del dataset para ver si se importó correctamente
print (datos_prot.head())


# Eliminar las filas conteniendo NaN para solo evaluar proteínas presentes en ambas condiciones
datos_prot_final = datos_prot.dropna()

# Transformar los datos a logaritmos en base 2 para que sean más sencillos de trabajar
cols_intensidad = ['WT-1', 'WT-2', 'WT-3', 'MUT-1', 'MUT-2', 'MUT-3']
for col in cols_intensidad:
    datos_prot_final[f'log2_{col}'] = np.log2(datos_prot_final[col])

# Chequear las transformaciones
print (datos_prot_final.head())

# Estadísticas descriptivas generales
print(datos_prot_final[['log2_WT-1', 'log2_WT-2', 'log2_WT-3', 'log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']].describe())

#[5 rows x 17 columns]
#         log2_WT-1    log2_WT-2    log2_WT-3   log2_MUT-1   log2_MUT-2   log2_MUT-3
#count  3549.000000  3549.000000  3549.000000  3549.000000  3549.000000  3549.000000
#mean     18.573178    18.541651    18.513589    18.505343    18.534105    18.518131
#std       2.369593     2.394758     2.426644     2.424304     2.395794     2.420087
#min      11.145779    10.624887    10.648151    10.195692    11.501155    10.295677
#25%      16.904235    16.827926    16.793692    16.802895    16.859595    16.811325
#50%      18.451976    18.424244    18.416138    18.385403    18.412553    18.396099
#75%      20.069072    20.082128    20.055897    20.029179    20.069072    20.055897
#max      29.055690    29.026966    29.076227    29.228485    29.118921    29.088916

cols_log = ['log2_WT-1', 'log2_WT-2', 'log2_WT-3', 'log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']

# Hacer un histograma para cada columna de datos logarítmicos
for col in cols_log:
    plt.hist(datos_prot_final[col], bins=30)
    plt.xlabel("Intensidad log2")
    plt.ylabel("Frecuencia")
    plt.title(f"Histograma {col}")
    #plt.show()

# Los histogramas parecieran corresponder a una distribución normal en todos los casos

# Calculo de la mediana para cada réplica
print(datos_prot_final[['log2_WT-1', 'log2_WT-2', 'log2_WT-3', 'log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']].median())

#log2_WT-1     18.451976
#log2_WT-2     18.424244
#log2_WT-3     18.416138
#log2_MUT-1    18.385403
#log2_MUT-2    18.412553
#log2_MUT-3    18.396099

# Se observa que la media es consistentemente ligeramente superior a la mediana (~0.1 log2), lo cual sugiere una leve asimetría a la derecha 
# A pesar de esto, las distribuciones mantienen una forma cercana a la normal

# Evaluación de asimetría 
skewness = datos_prot_final[cols_log].skew(axis=0, skipna=True, numeric_only=True)
print(skewness)

#log2_WT-1     0.288619
#log2_WT-2     0.295532
#log2_WT-3     0.260345
#log2_MUT-1    0.279568
#log2_MUT-2    0.304368
#log2_MUT-3    0.298010

# Todos los valores son positivos y están cerca de 0.3, indicando una ligera asimetría positiva (cola derecha más larga).
# Esto es común en datos biológicos y no indica una desviación fuerte de normalidad.

# Evaluación de curtosis
curtosis = datos_prot_final[cols_log].kurt(axis=0, skipna=True, numeric_only=True)
print(curtosis)

#log2_WT-1     0.140702
#log2_WT-2     0.063050
#log2_WT-3     0.092813
#log2_MUT-1    0.097409
#log2_MUT-2    0.078067
#log2_MUT-3    0.090928

# Las curtosis están muy cerca de 0 (entre 0.06 y 0.14), lo que indica distribuciones ligeramente más picudas que la normal pero sin ser extremo.
# No hay evidencia de distribuciones muy aplanadas ni muy sesgadas en forma de curtosis.

# Intervalos de confianza para cada réplica
# Como tengo un n > 30, utilizo la función de distribución normal estándar
for col in cols_log:
    data = datos_prot_final[col].dropna() 
    media = data.mean() # media
    sem = ss.sem(data)  # error estándar de la media
    
    ic = ss.norm.interval(confidence=0.95, loc=media, scale=sem)
    
    print(f"{col}: Media={media:.3f}, IC 95% normal = [{ic[0]:.3f}, {ic[1]:.3f}]")
#log2_WT-1: Media=18.573, IC 95% normal = [18.495, 18.651]
#log2_WT-2: Media=18.542, IC 95% normal = [18.463, 18.620]
#log2_WT-3: Media=18.514, IC 95% normal = [18.434, 18.593]
#log2_MUT-1: Media=18.505, IC 95% normal = [18.426, 18.585]
#log2_MUT-2: Media=18.534, IC 95% normal = [18.455, 18.613]
#log2_MUT-3: Media=18.518, IC 95% normal = [18.439, 18.598]

# Tamaño muestral
# En estudios de proteómica el objetivo no es validar una única diferencia entre condiciones, sino detectar múltiples cambios potencialmente relevantes.
# Además, existe consenso metodológico en el uso de al menos 3 réplicas biológicas independientes por grupo, lo cual es el diseño utilizado en este estudio.
# Por este motivo, no se calcula tamaño muestral en este análisis.

# Supuesto de normalidad. Test de normalidad
# H0: los datos se distribuyen normalmente.
# H1: los datos no se distribuyen normalmente.
for col in cols_log:
    resultado = ss.normaltest(datos_prot_final[col].dropna(), axis=0, nan_policy='propagate')
    print(f"Test de normalidad para {col}:")
    print(resultado)

# Test de normalidad para log2_WT-1:
# NormaltestResult(statistic=np.float64(50.229251934048705), pvalue=np.float64(1.238387408083189e-11))
# Test de normalidad para log2_WT-2:
# NormaltestResult(statistic=np.float64(50.350061784616074), pvalue=np.float64(1.1657971834272835e-11))
# Test de normalidad para log2_WT-3:
# NormaltestResult(statistic=np.float64(40.20352724919803), pvalue=np.float64(1.8617226450218886e-09))
# Test de normalidad para log2_MUT-1:
# NormaltestResult(statistic=np.float64(46.070101778384114), pvalue=np.float64(9.90842230891852e-11))
# Test de normalidad para log2_MUT-2:
# NormaltestResult(statistic=np.float64(53.54041475925321), pvalue=np.float64(2.365084465965096e-12))
# Test de normalidad para log2_MUT-3:
# NormaltestResult(statistic=np.float64(51.75026830115167), pvalue=np.float64(5.788579735336829e-12))

# El pvalue es menor a 0.05, por lo que se rechaza la hipótesis nula de normalidad; los datos no se distribuyen de manera normal.

# Supuesto de homocedasticidad de varianzas. Test de Levene.
# H0 = homocedasticidad de varianzas en el peso seco de las muestras es debido al azar.
# H1 = homocedasticidad de varianzas en el peso seco de las muestras no es debido al azar.

cols_WT = ['log2_WT-1', 'log2_WT-2', 'log2_WT-3']
cols_MUT = ['log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']

# Agrupar datos por condición concatenando todas las réplicas
wt_values = datos_prot_final[cols_WT].values.flatten()
mut_values = datos_prot_final[cols_MUT].values.flatten()

# Test de Levene para igualdad de varianzas (usamos center='median' para robustez)
levene_res = ss.levene(wt_values, mut_values, center='median')
print("Test de Levene para homogeneidad de varianzas:")
print(levene_res)
# Test de Levene para homogeneidad de varianzas:
# LeveneResult(statistic=np.float64(0.5626023957228993), pvalue=np.float64(0.4532218819401217))

# Como en el test de normalidad tuve que rechazar la hipótesis nula, tengo que hacer un test no parametrico para comparar los grupos.

# Test no paramétrico Mann-Whitney para comparar WT vs MUT (agrupando réplicas)
u_stat, p_value = ss.mannwhitneyu(wt_values, mut_values, alternative='two-sided')
print(f"Test Mann-Whitney para WT vs MUT:")
print(f"U-statistic = {u_stat:.3f}, p-value = {p_value:.3e}")



# Lo que yo quiero hacer en realidad es encontrar proteinas up o downreguladas, por lo que voy a hacer una comparación proteína a proteína usando Mann-Whitney U
# Test Mann-Whitney proteína por proteína
resultados = []

for index, fila in datos_prot_final.iterrows():
    wt_vals = pd.to_numeric(fila[['log2_WT-1', 'log2_WT-2', 'log2_WT-3']], errors='coerce').dropna()
    mut_vals = pd.to_numeric(fila[['log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']], errors='coerce').dropna()

    if len(wt_vals) > 0 and len(mut_vals) > 0:
        stat, pval = ss.mannwhitneyu(wt_vals, mut_vals, alternative='two-sided')
        resultados.append({'Proteina': fila['Genes'], 'U-statistic': stat, 'p-value': pval})
    else:
        resultados.append({'Proteina': fila['Genes'], 'U-statistic': np.nan, 'p-value': np.nan})


# Convertir a DataFrame
df_resultados = pd.DataFrame(resultados)

# Guardar a CSV con p-values corregidos
df_resultados.to_csv('resultado_mannwhitney_proteina.csv', index=False, float_format='%.6f')

# Mostrar primeros resultados con p corregido
print(df_resultados.head())

# Ordenar por p-valor corregido y mostrar top 10
top10_proteinas = df_resultados.sort_values(by='p-value').head(10)
print(top10_proteinas)

#                 Proteina  U-statistic  p-value  p-value_fdr  significativo_fdr
# 3544  LPU83_pLPU83d_1906          9.0      0.1     0.893955              False
# 3539  LPU83_pLPU83d_1846          0.0      0.1     0.893955              False
# 13                  repB          0.0      0.1     0.893955              False
# 1491          LPU83_1375          0.0      0.1     0.893955              False
# 1504                rpsF          0.0      0.1     0.893955              False
# 1429                sdhC          9.0      0.1     0.893955              False
# 135                dapB1          9.0      0.1     0.893955              False
# 140           LPU83_0326          0.0      0.1     0.893955              False
# 3489  LPU83_pLPU83d_1291          9.0      0.1     0.893955              False
# 1476          LPU83_3581          0.0      0.1     0.893955              False

# Tanto en la comparación global como proteína por proteína, se trató de grupos independientes (WT y MUT), sin apareamiento entre observaciones, razón por la cual se utilizó la prueba de Mann-Whitney.
# No se observan diferencias significativas para ninguna de las proteínas, ya que al observar los menores 10 pvalue puedo ver que ninguno es menor a 0.05.

# Como en proteómica solemos hacer T-test, quise intentar utilizarlo de todas maneras para observar los resultados
# Además, agregué el calulo del FoldChange porque para determinar si una proteína esta sobre o subexpresada, es necesario tener ambos valores

resultados_ttest_fc = []

for index, fila in datos_prot_final.iterrows():
    wt_vals = pd.to_numeric(fila[['log2_WT-1', 'log2_WT-2', 'log2_WT-3']], errors='coerce').dropna()
    mut_vals = pd.to_numeric(fila[['log2_MUT-1', 'log2_MUT-2', 'log2_MUT-3']], errors='coerce').dropna()

    if len(wt_vals) > 0 and len(mut_vals) > 0:
        stat, pval = ss.ttest_ind(wt_vals, mut_vals, equal_var=True)
        log2fc = mut_vals.mean() - wt_vals.mean()
        resultados_ttest_fc.append({'Proteina': fila['Genes'], 'T-statistic': stat, 'p-value': pval,  'log2FC': log2fc})
    else:
        resultados_ttest_fc.append({'Proteina': fila['Genes'], 'T-statistic': np.nan, 'p-value': np.nan,  'log2FC': np.nan})

df_ttest_fc = pd.DataFrame(resultados_ttest_fc)

# Guardar resultado
df_ttest_fc.to_csv('resultado_ttest_fc_proteina.csv', index=False)

# Top 10
print(df_ttest_fc.sort_values(by='p-value').head(10))

# Filtrar proteínas con p-valor significativo y log2FC alto o bajo
proteinas_significativas = df_ttest_fc[
    (df_ttest_fc['p-value'] < 0.05) &
    ((df_ttest_fc['log2FC'] > 2) | (df_ttest_fc['log2FC'] < -2))
]

# Guardar y mostrar resultados filtrados
proteinas_significativas.to_csv('proteinas_significativas_con_cambio_fc.csv', index=False)

print("\nProteínas con p < 0.05 y |log2FC| > 2:")
print(proteinas_significativas)

# Proteínas con p < 0.05 y |log2FC| > 2:
# Empty DataFrame
# Columns: [Proteina, T-statistic, p-value, log2FC]
# Index: []

# Los resultados coinciden con el test no paramétrico de que no existen proteínas sobre o subexpresadas
# En mis datos de proteómica, esto tiene sentido ya que el mutante es de una proteína hipotética que creemos es un regulador transcripcional los genes del sistema conjugativo.
# Estos genes no aparecen en la wt pero si en la mutante, cosa que no se muestra en este script, pero quería ver si afectaba a algo más global de la cepa en sí.
# Esto me dio una respuesta negativa, pudiendo observar que estaría afectando unicamente a nivel de proteínas ON-OFF, es decir en proteínas conjugativas
