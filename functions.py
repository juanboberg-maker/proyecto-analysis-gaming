# ========================================
# FUNCIONES Y CONFIGURACIONES UTILIZADAS
# ========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ===== CONFIGURACIÓN DE ESTILO =====
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# ===== FUNCIONES DE PANDAS =====
# Carga de datos
pd.read_csv()
df.groupby().agg()
df.reset_index()
df.merge()
df.nlargest()
df.mean()
df.sum()
df.unique()
df.itertuples()

# ===== FUNCIONES DE NUMPY =====
np.arange()
np.polyfit()
np.poly1d()
np.isnan()

# ===== FUNCIONES DE MATPLOTLIB =====
plt.subplots()
plt.tight_layout()
plt.savefig()
plt.close()
plt.colorbar()

# Métodos de Axes
ax.bar()
ax.barh()
ax.scatter()
ax.plot()
ax.set_xlabel()
ax.set_ylabel()
ax.set_title()
ax.set_xticks()
ax.set_xticklabels()
ax.set_ylim()
ax.set_xlim()
ax.axhline()
ax.legend()
ax.grid()
ax.text()
ax.annotate()

# Métodos de Bar
bar.get_height()
bar.get_width()
bar.get_x()
bar.get_y()

# ===== FUNCIONES DE PATHLIB =====
Path()

# ===== OPERACIONES ESPECÍFICAS DEL ANÁLISIS =====

# 1. Filtrado de datos
df[df['columna'] == valor]
df[df['columna'] > valor]
df[(condicion1) | (condicion2)]

# 2. Agregaciones por grupos
df.groupby('columna').agg({
    'col1': 'count',
    'col2': 'mean',
    'col3': 'sum'
})

# 3. Creación de columnas calculadas
df['nueva_columna'] = (df['col1'] > 0) | (df['col2'] > df['col3'])

# 4. Estadísticas descriptivas
df['columna'].mean()
df['columna'].sum()
len(df)
df['columna'].corr(df['otra_columna'])

# 5. Ordenamiento y selección top N
df.nlargest(n, 'columna')

# 6. Iteración sobre DataFrames
for _, row in df.iterrows():
    # procesamiento
for i, (bar, row) in enumerate(zip(bars, df.itertuples())):
    # procesamiento

# 7. Regresión lineal simple
z = np.polyfit(x, y, 1)  # Coeficientes de regresión
p = np.poly1d(z)         # Función polinómica
y_pred = p(x)            # Predicciones

# 8. Visualizaciones personalizadas
# - Gráficos de barras con anotaciones
# - Scatter plots con tamaño y color variables
# - Líneas de tendencia
# - Líneas horizontales de referencia
# - Colorbars para scatter plots
# - Anotaciones de texto en gráficos

# 9. Guardado de figuras
plt.savefig(ruta, dpi=300, bbox_inches='tight')