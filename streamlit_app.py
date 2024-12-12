import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="EMPLEATRONIX_GGE",
    layout="wide",
    page_icon="💸"
)

# Título de la aplicación
col_title1, col_title2 = st.columns(2)
with col_title1:
    st.title("EMPLEATRONIX_GGE")
with col_title2:
    st.title("Visualización de Salarios")

st.markdown("Todos los datos sobre los empleados en una aplicación.")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('data/employees.csv')
    # Renombrar la columna para usar guion bajo
    df = df.rename(columns={'full name': 'full_name'})
    return df

df = load_data()

# Crear dos columnas para la tabla y la gráfica
col_table, col_graph = st.columns(2)

# Mostrar tabla de datos en la primera columna
with col_table:
    st.markdown("### Datos de Empleados")
    st.dataframe(
        df[['full_name', 'salary', 'gender', 'email']].style.format({'salary': '{:.0f} €'}),
        hide_index=False,
        height=400
    )

# Controles y gráfica en la segunda columna
with col_graph:
    # Controles para la gráfica
    color = st.color_picker('Elige un color para las barras', '#00BCD4')
    show_names = st.toggle('Mostrar el nombre', True)
    show_values = st.toggle('Mostrar sueldo en la barra', False)  # Por defecto False

    # Crear gráfica de barras
    fig = go.Figure()

    # Añadir barras
    fig.add_trace(go.Bar(
        x=df['salary'],
        y=df['full_name'],
        orientation='h',
        marker_color=color,
        text=[f"{salary:.0f} €" for salary in df['salary']] if show_values else None,
        textposition='outside',
    ))

    # Configurar layout
    fig.update_layout(
        height=500,  # Aumentado la altura
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis_title="Salario (€)",
        yaxis_title="",
        showlegend=False,
        xaxis=dict(
            tickformat=",.0f",
            ticksuffix=" €"
        )
    )

    if not show_names:
        fig.update_layout(yaxis={'showticklabels': False})

    # Mostrar gráfica
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("\n\n---\n\n*Hecho por [Germán García Estevez](https://www.linkedin.com/in/germangarest)*")