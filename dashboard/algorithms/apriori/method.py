import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from apyori import apriori


def method(transac_data):
    graph, dataSet = process_data(transac_data)
    res = application(dataSet,0.0045,0.2,3)
    return graph, res


def process_data(transac_data):
    #Se incluyen todas las transacciones en una sola lista
    Transacciones = transac_data.values.reshape(-1).tolist() 

    #Se crea una matriz (dataframe) usando la lista y se incluye una columna 'Frecuencia'
    Lista = pd.DataFrame(Transacciones)
    Lista['Frecuencia'] = 1

    #Se agrupa los elementos
    Lista = Lista.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True) #Conteo
    Lista['Porcentaje'] = (Lista['Frecuencia'] / Lista['Frecuencia'].sum()) #Porcentaje
    Lista = Lista.rename(columns={0 : 'Item'})

    TransaccionesLista = transac_data.stack().groupby(level=0).apply(list).tolist() 

    return img_gen(Lista), TransaccionesLista


def img_gen(Lista):
    fig = go.Figure([go.Bar(x=Lista['Frecuencia'], y=Lista['Item'], 
                    orientation='h',marker=dict(color='green'))])
    fig.update_layout(
        title='Distribución de los datos',
        xaxis_title='Frecuencia',
        yaxis_title='Item',
        height=800,
        font=dict(
            family='Arial',
            size=12
        )
    )
    return fig

def application(dataSet, support, confidence, lift):
    ReglasC1 = apriori(dataSet, 
                   min_support=support, 
                   min_confidence=confidence, 
                   min_lift=lift)
    ResultadosC1 = list(ReglasC1)
    resultados = []
    for item in ResultadosC1:
        Emparejar = item[0]
        items = [x for x in Emparejar]
        resultados.append({
            'Regla': str(item[0]),
            'Soporte': str(item[1]),
            'Confianza': str(item[2][0][2]),
            'Elevación': str(item[2][0][3])
        })
    
    df_resultados = pd.DataFrame(resultados)
    return df_resultados