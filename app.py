# Para manejo de datos en tablas, lo que permite llevar procesos de limpieza, organización y análisis de datos.
import pandas as pd 
# Streamlit me permite crear la aplicación web interactiva.
import streamlit as st 
# Aunque no hago uso de ella en este código, si es util para realizar gráficos tradicionales (barras, histogramas, etc.) de ser necesario.
import matplotlib.pyplot as plt 
# Esta libreria me permite crear gráficos interactivos y visualizaciones rápidas como el Treemap creado en este código.
import plotly.express as px

# Estoy abriendo el archico 'datos_anteproyecto.csv' y luego se carga en un Dataframe de python llamado apgn, que me permite visualizar los datos en el Treemap.
apgn = pd.read_csv('datos_anteproyecto.csv') 

# Asigno un encabezado de titulo para la aplicación web en Streamlit
st.title("Análisis de datos macroeconómicos")

# 'st.write' imprime texto y aqui lo uso para describir vrebemente mi trabajo.
st.write("Acontinuación se elaboró una tabla tipo Treemap con la ayuda del gráficador rapido **plotly.express** que permite visualizar los datos, anteriormente limpiados, en forma de gráfico jerárquico en el que cada rectángulo representa un elemento y el tamaño esta representado por un valor numérico.") 

# Se crea una pestaña por estética para que no se vea plana la aplicación, la coma continua a 'tab2' indica que solo hay una pestaña aunque la sintaxis espera una tupla de más elementos.
tab1, = st.tabs(['Gráfico de análisis'])

# Indíca que el codigo posterior esta indexado en la pestaña.
with tab1:
    # Se asigna un subtitulo para la pestaña
    st.subheader("Programa Anteproyecto 2026")

    # Me permite escribir en Markdown, es decir, listas, párrafos, negrillas (** **), etc. Aqui describo el gráfico, sus colores y tipos de asignación presupuestal.
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
    # Se crea un objeto de tipo figura de Plotly, que guarda toda la información requerida para realizar el gráfico de Treemap.
    fig =  px.treemap(data_frame = apgn,
                      # 'ps.constant' Establece la gerarquia de los rectángulos, siendo PGN el nodo principal, dividido por rectangulos en el que cada uno es un sector y a su vez dividido por el tipo de gasto.
           path=[px.Constant("PGN"),
                 "Nombre Sector",
                 "Tipo de gasto"],
            values='Valor',
            color="Tipo de gasto", 
            color_discrete_sequence=px.colors.qualitative.Pastel )
    # Inserta el gráfico de Plotly en la app web.
    st.plotly_chart(fig)

#Fin
