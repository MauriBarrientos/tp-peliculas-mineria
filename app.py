from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import numpy as np

# Cargar el dataframe desde el archivo CSV
df = pd.read_csv('movies.csv')

#Grafico de peliculas más taquilleras
def grafico1():
    # Convertir la columna 'Gross LT Worldwide' a valores numéricos
    df['Worldwide LT Gross'] = df['Worldwide LT Gross'].replace({'\$': '', ',': '', 'M': '*1e6', 'B': '*1e9'}, regex=True).map(pd.eval).astype(float)
    top_peliculas = df.sort_values(by='Worldwide LT Gross', ascending=False)
    
    n = 5
    top_peliculas = top_peliculas.head(n)
    # Crear el gráfico de barras
    fig = px.bar(top_peliculas, x='Movie Title', y='Worldwide LT Gross', 
                 title='Peliculas más taquilleras', 
                 labels={'Movie Title': 'Película', 'Worldwide LT Gross': 'Ingresos (en miles de millones)'},
                 color= 'Worldwide LT Gross', color_continuous_scale='RdBu')
    
    return fig
fig1 = grafico1()

#Grafico de películas más costosas
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
    
    top_peliculas_costosas = df.sort_values(by='Gross', ascending=False)
    
    n = 5  
    top_peliculas_costosas = top_peliculas_costosas.head(n)
    
    # Crear el gráfico de barras
    fig2 = px.bar(top_peliculas_costosas, x='Movie Title', y='Gross', 
                 title='Películas más costosas', 
                 labels={'Movie Title': 'Película', 'Gross': 'Costo de Producción (en millones de dólares)'})
    
    return fig2
fig2 = grafico2()


#Grafico de presupuesto a través de los años
def grafico3():
    df['Year of Realease'] = pd.to_datetime(df['Year of Realease'], format='%Y')

    # Calcular el presupuesto promedio por año
    presupuesto_promedio = df.groupby(df['Year of Realease'].dt.year)['Gross'].mean()

    ultimos_100_anios = presupuesto_promedio.tail(100) # Filtrar los últimos 100 años

    # Crear el gráfico de líneas
    fig3 = px.line(x=ultimos_100_anios.index, y=ultimos_100_anios.values, title='Aumento del presupuesto de películas en los últimos 100 años',
                labels={'x': 'Año', 'y': 'Presupuesto promedio (en millones de dólares)'})
    return fig3
fig3 = grafico3()

#Grafico de películas más baratas
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
  
    top_peliculas_menos_costosas = df.sort_values(by='Gross', ascending=True)
    
    top_peliculas_menos_costosas = top_peliculas_menos_costosas.head(n) #Tomar las n primeras películas menos costosas
    
    # Crear el gráfico de barras
    fig4 = px.bar(top_peliculas_menos_costosas, x='Movie Title', y='Gross', 
                 title='Películas con menor presupuesto', 
                 labels={'Movie Title': 'Película', 'Gross': 'Costo de Producción (en dólares)'})
    
    return fig4
fig4= grafico4(df)

#Gráfico de los 5 generos principales
def grafico5():
    porcentaje_genero = df['Genre'].value_counts()
    porcentaje_genero = porcentaje_genero.head(5)
    fig5= px.pie(values=porcentaje_genero.values, names=porcentaje_genero.index, title='Distribución de generos' )
    return fig5

fig5= grafico5()


#Grafico de peliculas con mayor puntuación
def grafico6():
    top_peliculas_meta = df.sort_values(by='Metascore', ascending=False).head(10)
    fig6= px.bar(top_peliculas_meta, x='Movie Title', y='Metascore',
                 title='Peliculas con mayor puntuación',
                 labels={'Movie Title': 'Película', 'Metascore': 'Puntuación'})
    return fig6
fig6= grafico6()

# Crear la aplicación Dash
app = Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1('Éxitos de peliculas en taquilla'),
    dcc.Graph(id='graph-pelicula-taquillera', figure=fig1),
    dcc.Graph(id='graph-pelicula-costosa', figure=fig2),
    dcc.Graph(id='graph-aumento-presupuesto', figure=fig3),
    dcc.Graph(id='graph-pelicula-menos-costosa', figure=fig4),
    dcc.Graph(id='graph-porcentaje-genero', figure=fig5),
    dcc.Graph(id='graph-pelicula-meta', figure=fig6)
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
