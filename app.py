import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px
apgn = pd.read_csv('datos_anteproyecto.csv') 
ran = pd.read_csv('datos_random.csv')

st.title("Análisis de datos macroeconómicos")
st.write("Acontinuación se elaboró una tabla tipo Treemap con la ayuda del gráficador rapido 'plotly.express' que permite visualizar los datos, anteriormente limpiados, en forma de gráfico jerárquico en el que cada rectángulo muestra la proyección de gasto de cada una de las dependencias del estado colombiano con base en el Programa Anteproyecto 2026 realizado por el Ministerio de Hacienda y Crédito Público de Colombia") 

tab2, = st.tabs(['Gráfico de análisis'])

with tab2:
    fig =  px.treemap(data_frame = apgn,
           path=[px.Constant("PGN"),
                 "Nombre Sector",
                 "Tipo de gasto"],
            values='Valor',
            color="Tipo de gasto", 
            color_discrete_sequence=px.colors.qualitative.Pastel )

    st.plotly_chart(fig)
