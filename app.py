from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import numpy as np

# Cargar el dataframe desde el archivo CSV
df = pd.read_csv('movies.csv')

# # Crear el gráfico de barras
def grafico1():
    # Convertir la columna 'Gross LT Worldwide' a valores numéricos
    df['Worldwide LT Gross'] = df['Worldwide LT Gross'].replace({'\$': '', ',': '', 'M': '*1e6', 'B': '*1e9'}, regex=True).map(pd.eval).astype(float)

    # Ordenar el dataframe por 'Worldwide LT Gross' de manera descendente
    top_peliculas = df.sort_values(by='Worldwide LT Gross', ascending=False)
    
    n = 5  # Define el número de películas a considerar
    top_peliculas = top_peliculas.head(n)
    
    # Crear el gráfico de barras
    fig = px.bar(top_peliculas, x='Movie Title', y='Worldwide LT Gross', 
                 title='Peliculas más taquilleras', 
                 labels={'Movie Title': 'Película', 'Worldwide LT Gross': 'Ingresos (en miles de millones)'})
    
    return fig

fig1 = grafico1()

def grafico2():
    # Eliminar el símbolo '$' de la columna 'Gross'
    df['Gross'] = df['Gross'].str.replace('$', '')
    
    # Eliminar las comas ',' de la columna 'Gross'
    df['Gross'] = df['Gross'].str.replace(',', '')
    
    # Reemplazar 'M' por 'e6' y 'B' por 'e9'
    df['Gross'] = df['Gross'].str.replace('M', 'e6').str.replace('B', 'e9')

     # Reemplazar '******' con NaN
    df['Gross'] = df['Gross'].replace('******', np.nan)
    
    # Convertir la columna 'Gross' a tipo numérico
    df['Gross'] = df['Gross'].astype(float)
    
    # Ordenar el dataframe por 'Production Budget' de manera descendente
    top_peliculas_costosas = df.sort_values(by='Gross', ascending=False)
    
    n = 5  
    top_peliculas_costosas = top_peliculas_costosas.head(n)
    
    # Crear el gráfico de barras
    fig2 = px.bar(top_peliculas_costosas, x='Movie Title', y='Gross', 
                 title='Películas más costosas', 
                 labels={'Movie Title': 'Película', 'Gross': 'Costo de Producción (en millones de dólares)'})
    
    return fig2

fig2 = grafico2()


def grafico3():
    df['Year of Realease'] = pd.to_datetime(df['Year of Realease'], format='%Y')

    # Calcular el presupuesto promedio por año
    presupuesto_promedio = df.groupby(df['Year of Realease'].dt.year)['Gross'].mean()

    # Filtrar los últimos 100 años
    ultimos_100_anios = presupuesto_promedio.tail(100)

    # Crear el gráfico de líneas
    fig3 = px.line(x=ultimos_100_anios.index, y=ultimos_100_anios.values, title='Aumento del presupuesto de películas en los últimos 100 años',
                labels={'x': 'Año', 'y': 'Presupuesto promedio (en millones de dólares)'})
    return fig3

fig3 = grafico3()

def grafico4(df, n=5):
    # Verificar si los valores en la columna 'Gross' son de tipo string
    if df['Gross'].dtype == 'O':
        # Eliminar el símbolo '$' de la columna 'Gross'
        df['Gross'] = df['Gross'].str.replace('$', '')
        
        # Eliminar las comas ',' de la columna 'Gross'
        df['Gross'] = df['Gross'].str.replace(',', '')
        
        # Reemplazar 'M' por 'e6' y 'B' por 'e9'
        df['Gross'] = df['Gross'].str.replace('M', 'e6').str.replace('B', 'e9')

         # Reemplazar '******' con NaN
        df['Gross'] = df['Gross'].replace('******', pd.NA)
        
        # Convertir la columna 'Gross' a tipo numérico
        df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
  
    # Ordenar el dataframe por 'Gross' de manera ascendente para obtener las películas con menor presupuesto
    top_peliculas_menos_costosas = df.sort_values(by='Gross', ascending=True)
    
    # Tomar las n primeras películas menos costosas
    top_peliculas_menos_costosas = top_peliculas_menos_costosas.head(n)
    
    # Crear el gráfico de barras
    fig4 = px.bar(top_peliculas_menos_costosas, x='Movie Title', y='Gross', 
                 title='Películas con menor presupuesto', 
                 labels={'Movie Title': 'Película', 'Gross': 'Costo de Producción (en dólares)'})
    
    return fig4

fig4= grafico4(df)


# Crear la aplicación Dash
app = Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Éxitos de peliculas en taquilla'),
    dcc.Graph(id='graph-pelicula-taquillera', figure=fig1),
    dcc.Graph(id='graph-pelicula-costosa', figure=fig2),
    dcc.Graph(id='graph-aumento-presupuesto', figure=fig3),
    dcc.Graph(id='graph-pelicula-menos-costosa', figure=fig4)
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
