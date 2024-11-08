import pandas as pd
import numpy as np

# Definir los nombres de las columnas
columnas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# Leer el archivo CSV sin encabezados y asignar nombres de columnas
df_iris = pd.read_csv('bezdekIris.data', header=None, names=columnas)

# Mostrar las primeras filas del DataFrame
print("Primeras 5 filas del dataset:")
print(df_iris.head())

# Información básica del DataFrame
print("\nInformación del DataFrame:")
print(df_iris.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df_iris.describe())

# Conteo de especies
print("\nDistribución de especies:")
print(df_iris['species'].value_counts())

# Verificar si hay valores nulos
print("\nValores nulos en el dataset:")
print(df_iris.isnull().sum())