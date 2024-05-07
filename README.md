# Nombre de la Aplicación

Top películas mas taquilleras

## Descripción
Esta aplicación utiliza datos de las 1000 películas más taquilleras de todos los tiempos para proporcionar visualizaciones interactivas sobre diferentes aspectos de estas películas, incluyendo sus ingresos, costos de producción, puntajes de críticas y géneros predominantes.

## Gráficos Disponibles

1. **Películas Más Taquilleras:** Muestra las cinco películas más taquilleras en un gráfico de barras, con los ingresos mundiales como eje y.
   
2. **Películas Más Costosas:** Presenta las cinco películas con los mayores costos de producción en un gráfico de barras, con el costo de producción como eje y.

3. **Aumento del Presupuesto a lo Largo del Tiempo:** Muestra cómo ha aumentado el presupuesto promedio de las películas en los últimos 100 años en un gráfico de líneas.

4. **Películas con Menor Presupuesto:** Muestra las cinco películas con los presupuestos más bajos en un gráfico de barras, con el costo de producción como eje y.

5. **Distribución de Géneros:** Muestra la distribución de los cinco géneros principales en un gráfico de pastel.

6. **Películas con Mayor Puntuación Metascore:** Muestra las diez películas con las puntuaciones de Metascore más altas en un gráfico de barras, con el Metascore como eje y.


## Requisitos

- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.

## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:

```bash
pip install pandas
```

```bash
pip install dash
```

```bash
pip install plotly
```

## Archivo y Uso

Para ejecutar el siguiente archivo es necesario escribir este script en la terminal:

```bash
python app.py
```

A continuación se ejecutara el servidor y en la terminal te saldra el puerto `http://127.0.0.1:8050/`, es ahí donde debes de ingresar para visualizar los gráficos.