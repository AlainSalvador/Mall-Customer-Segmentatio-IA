# Mall-Customer-Segmentatio-IA
Optimizar estrategias de marketing agrupando clientes por comportamiento de compra

Solución: "Modelo de Machine Learning no supervisado que detectó 5 perfiles de consumidor distintos".

## Descripción del Proyecto
Este proyecto implementa un algoritmo de **Machine Learning No Supervisado** (K-Means) para segmentar clientes de un centro comercial. El objetivo es transformar una base de datos plana en **5 perfiles de comportamiento** (Clusters) para diseñar estrategias de marketing personalizadas.

## Tecnologías y Herramientas
* **Python 3.9+**
* **Scikit-Learn:** Para el algoritmo K-Means.
* **Pandas & Numpy:** Manipulación de datos.
* **Seaborn & Matplotlib:** Visualización de datos.
* **FPDF:** Generación automatizada de reportes ejecutivos.

## Metodología
1.  **Exploración de Datos:** Análisis de distribución de *Ingresos Anuales* vs *Puntuación de Gastos*.
2.  **Elbow Method (Método del Codo):** Se determinó matemáticamente que el número óptimo de clusters es **k=5**.
3.  **Modelado:** Entrenamiento del modelo K-Means para agrupar a los clientes.
4.  **Reporting:** Generación automática de un PDF con estrategias de negocio para cada grupo.

## Resultados (Clusters Detectados)
La IA identificó los siguientes grupos estratégicos:
1.  **Los VIP:** Altas ganancias y gastos (Objetivo de fidelización premium).
2.  **Los Impulsivos:** Bajas ganancias pero altos gastos (Objetivo de promociones flash).
3.  **Los Cautos:** Altas ganancias pero bajos gastos (Objetivo de marketing racional).
4.  **Estándar:** Comportamiento promedio.
5.  **Ahorradores:** Bajos ingresos y bajos gastos.

## Entregables
El repositorio incluye un script que genera automáticamente el archivo `Estrategia_Marketing_IA.pdf`, listo para ser presentado a directivos o clientes.
