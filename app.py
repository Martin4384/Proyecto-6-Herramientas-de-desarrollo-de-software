import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Grafico de información de vehiculos') 
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
#hist_button = st.button('Construir histograma') # crear un botón
build_histogram = st.checkbox('Construir un histograma')
        
if build_histogram: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Creación de un grafico de Dispersion relacion Precio y Kilometraje')
            
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

