import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px
apgn = pd.read_csv('datos_anteproyecto.csv') 
ran = pd.read_csv('datos_random.csv')

st.title("Análisis de datos macroeconómicos")
st.write("Acontinuación se elaboró una tabla tipo Treemap con la ayuda del gráficador rapido 'plotly.express' que permite visualizar los datos, anteriormente limpiados, en forma de gráfico jerárquico en el que cada rectángulo representa un elemento y el tamaño esta representado por un valor numérico.") 

tab2, = st.tabs(['Gráfico de análisis'])

with tab2:
    st.subheader("Programa Anteproyecto 2026")


        st.markdown("""
    Este gráfico muestra la proyección presupuestal de cada una de las dependencias 
del Estado colombiano con base en el **Programa Anteproyecto 2026** realizado por 
el **Ministerio de Hacienda y Crédito Público de Colombia** el 4 de abril del 2025.

- El tamaño de cada rectángulo demuestra la proporción del presupuesto proyectado.  
- Existen tres tipos de asignación presupuestal:  
  **A**: Presupuesto de Funcionamiento.  
  **B**: Presupuesto de servicio de la deuda pública.  
  **C**: Presupuesto de inversión.
    """)
    fig =  px.treemap(data_frame = apgn,
           path=[px.Constant("PGN"),
                 "Nombre Sector",
                 "Tipo de gasto"],
            values='Valor',
            color="Tipo de gasto", 
            color_discrete_sequence=px.colors.qualitative.Pastel )

    st.plotly_chart(fig)
