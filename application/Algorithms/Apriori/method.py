import pandas as pd
import plotly.graph_objects as go
from apyori import apriori
import json
import plotly

def process_dataGraph(transac_data):
    # Se incluyen todas las transacciones en una sola lista
    Transacciones = transac_data.values.reshape(-1).tolist()

    # Se crea una matriz (dataframe) usando la lista y se incluye una columna 'Frecuencia'
    Lista = pd.DataFrame(Transacciones)
    Lista['Frecuencia'] = 1

    # Se agrupa los elementos
    Lista = Lista.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True)
    Lista['Porcentaje'] = (Lista['Frecuencia'] / Lista['Frecuencia'].sum())
    Lista = Lista.rename(columns={0: 'Item'})

    # Genera la gráfica utilizando Plotly
    fig = go.Figure([go.Bar(x=Lista['Frecuencia'], y=Lista['Item'], orientation='h', marker=dict(color='green'))])
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
    #Convirtiendo la imagen a JSON
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json

def application(dataSet, support, confidence, lift):
    dataSet = dataSet.stack().groupby(level=0).apply(list).tolist() 
    ReglasC1 = apriori(dataSet, 
                   min_support=support/100, 
                   min_confidence=confidence/100, 
                   min_lift=lift)
    ResultadosC1 = list(ReglasC1)
    resultados = []
    for item in ResultadosC1:
        Emparejar = item[0]
        items = [x for x in Emparejar]
        regla = ', '.join(items).strip('{}')
        antecedente = ', '.join(item[2][0][0]).strip('{}')
        consecuente = ', '.join(item[2][0][1]).strip('{}')
        resultados.append({
            'Regla': regla,
            'Antecedente': antecedente,
            'Consecuente': consecuente,
            'Soporte': "{:.3f}%".format(item[1] * 100),
            'Confianza': "{:.3f}%".format(item[2][0][2] * 100),
            'Elevación': "{:.3f}".format(item[2][0][3])
        })
    
    df_resultados = pd.DataFrame(resultados)
    return df_resultados

