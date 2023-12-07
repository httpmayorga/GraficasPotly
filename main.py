import pandas as pd
import plotly.graph_objects as go

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

orden_materias = ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']
df['materia'] = pd.Categorical(df['materia'], categories=orden_materias, ordered=True)

fig = go.Figure()
#Crear el diagrama de cajas
for materia in orden_materias:
    data_materia = df[df['materia'] == materia]
    fig.add_trace(go.Box(y=data_materia['nota'], name=materia))

fig.update_layout(title='Distribución de Notas de Estudiantes por Materia',xaxis_title='Materias',yaxis_title='Notas')

# Crear el pie chart
cantidad_aprobados = len(df[df['aprobado'] == 'Sí'])
cantidad_no_aprobados = len(df[df['aprobado'] == 'No'])

labels = ['Aprobados', 'No Aprobados']
values = [cantidad_aprobados, cantidad_no_aprobados]
colors = ['#ff9999', '#66b3ff']

fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
fig_pie.update_traces(textinfo='percent+label')
fig_pie.update_layout(title='Distribución de Estudiantes Aprobados y No Aprobados')

# Mostrar ambas visualizaciones
fig.show()
fig_pie.show()
