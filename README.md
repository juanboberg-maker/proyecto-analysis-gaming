# Proyecto: Análisis de hardware gaming en e‑commerce
## 1. Descripción del proyecto
Proyecto individual de análisis de datos centrado en hardware gaming nuevo (no reacondicionado) vendido online.
El objetivo es analizar cómo influyen las reseñas, la marca, el precio (segmentado en gamas) y los descuentos en la popularidad de productos de varias subcategorías de gaming en un e‑commerce español (PC Componentes) y compararlo con un dataset externo de Kaggle sobre ventas y valoraciones de productos gaming/electrónica.

## 2. Objetivos
Extraer datos de hardware gaming nuevo de PC Componentes mediante web scraping (o API si fuera posible).

Integrar estos datos con un dataset de Kaggle que contenga información de ventas/valoraciones de productos gaming o electrónicos.

Realizar el análisis de datos combinando Python y SQL:

Limpieza y preparación de datos en Python.

Creación de tablas y consultas analíticas en SQL.

Segmentación de los productos en gamas de precio usando percentiles.

Visualizaciones finales en Python para apoyar una presentación de ~7 minutos.

## 3. Alcance del análisis
3.1 Subcategorías analizadas
El análisis se centra en productos de hardware gaming nuevo (no reacondicionado) de las siguientes subcategorías en PC Componentes:

PCs / Ordenadores gaming

Monitores

Teclados

Ratones

Mandos

Cascos

3.2 Fuentes de datos
Fuente 1 – PC Componentes (web scraping)

Tienda online española de informática y tecnología.

Scraping de las páginas de listado de productos de las subcategorías anteriores.

Variables objetivo por producto:

Nombre del producto

Marca

Subcategoría

Precio actual

Precio original (para calcular descuento porcentual, si está disponible)

Descuento porcentual (calculado)

Valoración media (estrellas)

Número de opiniones

Información adicional relevante (por ejemplo, etiquetas tipo “top ventas”, si se muestran)

Fuente 2 – Dataset de Kaggle (ventas/valoraciones gaming/electrónica)

Dataset con productos gaming/electrónicos que contenga, idealmente:

Nombre / identificador del producto

Marca

Categoría / tipo de producto

Precio

Ventas o unidades vendidas

Valoraciones (rating medio, número de reseñas)

Uso principal:

Complementar y dar contexto a los patrones observados en PC Componentes.

Analizar la relación entre marca, rating y ventas en un dataset más amplio.

## 4. Segmentación por gamas de precio
Para controlar el efecto del precio en la popularidad y las reseñas, se segmentan los productos en gamas de precio utilizando percentiles por subcategoría:

La segmentación se realiza dentro de cada subcategoría (PC, monitores, teclados, ratones, mandos, cascos), ya que los rangos de precio naturales son distintos entre ellas.

Se calculan los percentiles de precio y se asigna a cada producto una de las siguientes gamas:

Gama alta: productos en el percentil 90 o superior de precio (top 10% más caros).

Gama media: productos entre los percentiles 65 y 90 de precio.

Gama baja: productos por debajo del percentil 65 de precio.

Esta segmentación permite:

Comparar popularidad (número de opiniones) y rating controlando por gama de precio.

Analizar si los patrones observados en las hipótesis (peso de marca, reseñas, descuentos) se mantienen dentro de cada gama o cambian entre gama baja, media y alta.

Investigar, en particular, si en la gama alta los descuentos porcentuales tienen un impacto mayor en la popularidad (H3), al compensar el precio más elevado.

## 5. Hipótesis
Hipótesis 1 (H1) – “Los más populares tienen mejores reseñas”
H1: Dentro de cada subcategoría de hardware gaming nuevo en PC Componentes (PC, monitores, teclados, ratones, mandos y cascos), los productos del top 10% por número de opiniones presentan, en promedio, una valoración media de estrellas significativamente mayor que el resto de productos de su subcategoría, incluso al controlar por gama de precio.

Popularidad ≈ número de opiniones (proxy de ventas).

Grupo A: top 10% de productos por número de opiniones en cada subcategoría.

Grupo B: 90% restante de productos en esa subcategoría.

Se puede realizar la comparación global y también dentro de cada gama de precio (baja, media, alta).

Hipótesis 2 (H2) – “Marca vs reseñas”
H2: En el catálogo de hardware gaming nuevo de PC Componentes, la marca del producto tiene mayor impacto en la popularidad (número de opiniones) que la valoración media de reseñas; es decir, las marcas con más productos en el top 10% de popularidad no coinciden necesariamente con las que tienen mejores valoraciones medias, incluso cuando se comparan productos dentro de una misma gama de precio.

Popularidad ≈ número de opiniones.

Para cada subcategoría y marca se analiza:

Popularidad media (opiniones por producto).

Valoración media.

Porcentaje de productos de esa marca que están en el top 10% de popularidad.

La comparación puede hacerse:

Global.

Y segmentada por gama de precio (para evitar que las marcas caras parezcan más “populares” solo por su posición en gama alta).

Hipótesis 3 (H3) – “Categoría que rompe el patrón + descuentos”
H3: Existe al menos una de las subcategorías analizadas (PC, monitores, teclados, ratones, mandos o cascos) en la que la relación entre marca, reseñas y popularidad se desvía del patrón general, y en esa subcategoría el descuento porcentual sobre el precio tiene un papel más relevante en la popularidad (número de opiniones), especialmente entre el top 10% de productos y dentro de la gama alta de precio.

Se mantiene el criterio de top 10% como grupo principal de productos para comparar.

Se utiliza el descuento porcentual como tercer factor explicativo.

Se analiza, por subcategoría y gama de precio:

Diferencias de descuento medio entre top 10% y resto.

Si en alguna categoría, dentro de la gama alta, los productos populares tienen descuentos claramente mayores que en otras categorías, lo que sugiere que el descuento compensa el precio.

## 6. Enfoque técnico (Python + SQL)
6.1 Python
Scraping de PC Componentes (requests + BeautifulSoup, u otra librería).

Limpieza de datos con Pandas:

Normalización de nombres de marca y subcategoría.

Conversión de precios y descuentos a formato numérico.

Cálculo de descuento porcentual.

Cálculo de percentiles de precio por subcategoría y asignación de la columna price_tier (gama baja, media, alta).

Creación de indicadores de popularidad (top 10% por número de opiniones).

Carga de datos a la base de datos SQL (por ejemplo, usando SQLAlchemy / to_sql).

Análisis estadístico complementario y visualizaciones finales (gráficos por categoría, marca y gama de precio).

6.2 SQL
Definición de tablas principales:

pccomponentes_productos (datos scrapeados con columnas como precio, descuento_pct, price_tier, rating, num_opiniones, top_10_popularidad, etc.).

kaggle_productos (datos del dataset externo).

Consultas de agregación:

Popularidad y rating medio por subcategoría, marca y gama de precio.

Identificación del top 10% por opiniones en cada subcategoría.

Joins y comparaciones con el dataset de Kaggle para analizar patrones generales de ventas vs reseñas y marca.

## 7. Entregables
Código en Python para:

Scraping de PC Componentes.

Limpieza, cálculo de percentiles/gamas de precio y preparación de datos.

Análisis y visualización final.

Esquema SQL (scripts de creación de tablas y consultas clave).

Presentación (~7 minutos) explicando:

Contexto y fuentes de datos.

Hipótesis planteadas.

Metodología (Python + SQL + segmentación por gamas de precio).

Resultados principales y visualizaciones.

Conclusiones y posibles extensiones futuras del proyecto.
