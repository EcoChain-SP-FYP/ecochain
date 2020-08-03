import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
from modules.simSensor import DHT22, light, moisture, CO2
from datetime import datetime, timedelta
from contract import contractClass
import sys
from collections import deque

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

sensors = []
values = []
time = []

ctmvalues = []
ctmsensor = []

hlvalues = []
hlsensor = []

time = deque(maxlen=40)
values = deque(maxlen=40)
sensors = deque(maxlen=40)

ctmvalues = deque(maxlen=3)
ctmsensor = deque(maxlen=3)

hlvalues = deque(maxlen=1)
#hlsensor = deque(maxlen=2)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


app.layout = html.Div(
    children=[
        html.H1(children="Sensor Datas"),
        html.Div(
            id="Temperature",
            children="""
        Dash: A web application framework for Python.
    """,
        ),
        dcc.Graph(id="live-graph-sensors"),
        dcc.Interval(id="interval-sensors", interval= 5 * 1000, n_intervals=0),
        html.Div(
            id="CO2",
            children="""
        Bar chart (CO2, Temperature & Moisture)
    """,
        ),
        dcc.Graph(id="live-graph-CO2"),
        dcc.Interval(id="interval-CO2", interval= 5 * 1000, n_intervals=0),
        html.Div(
            id="Humid",
            children="""
        Gauge chart (Humidity)
    """,
        ),
        dcc.Graph(id="live-graph-Humid"),
        dcc.Interval(id="interval-Humid", interval= 5 * 1000, n_intervals=0),
        html.Div(
            id="Light",
            children="""
        Gauge chart (Light)
    """,
        ),
        dcc.Graph(id="live-graph-Light"),
        dcc.Interval(id="interval-Light", interval= 5 * 1000, n_intervals=0),
    ]
)


@app.callback(
    Output("live-graph-sensors", "figure"), [Input("interval-sensors", "n_intervals")]
)
def updateSensor(n):
    sensorValues = contract.getLatestTransactionInputValues()
    sensors.extend(("Temperature", "Humidity", "Light", "Moisture", "CO2"))
    values.extend(
        (
            sensorValues[0],
            sensorValues[1],
            sensorValues[2],
            sensorValues[4],
            sensorValues[5],
        )
    )
    time.extend(
        (
            sensorValues[6],
            sensorValues[6],
            sensorValues[6],
            sensorValues[6],
            sensorValues[6],
        )
    )

    df = pd.DataFrame({"Sensors": sensors, "Values": values, "Time": time})
    fig = px.line(df, x="Time", y="Values", color="Sensors")
    fig.data[0].update(mode="markers+lines")
    fig.data[1].update(mode="markers+lines")
    fig.data[2].update(mode="markers+lines")
    fig.data[3].update(mode="markers+lines")
    fig.data[4].update(mode="markers+lines")
    fig.update_layout(xaxis=dict(range=[1, 4]))
    return fig

@app.callback(
    Output("live-graph-CO2", "figure"), [Input("interval-CO2", "n_intervals")]
)
def updateco2(n):
    sensorValues = contract.getLatestTransactionInputValues()
    ctmvalues.extend(
        (
            sensorValues[5],
            sensorValues[0],
            sensorValues[4],
        )
    )
    ctmsensor.extend(
        (
            "CO2", "Temperature", "Moisture"
        )
    )

    df = pd.DataFrame({"Values": ctmvalues, "Sensors": ctmsensor})
    fig = px.bar(df, x="Sensors", y="Values")
    return fig

@app.callback(
    Output("live-graph-Humid", "figure"), [Input("interval-Humid", "n_intervals")]
)
def updatehumd(n):
    sensorValues = contract.getLatestTransactionInputValues()
    humid = sensorValues[1]


    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = float(humid),
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Humidity"}))
    
    return fig

@app.callback(
    Output("live-graph-Light", "figure"), [Input("interval-Light", "n_intervals")]
)
def updatelight(n):
    sensorValues = contract.getLatestTransactionInputValues()
    light = sensorValues[2]


    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = float(light),
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Light"}))
    
    return fig

if __name__ == "__main__":
    # try:
    # blockchain_address = f"http://{sys.argv[1]}"
    # deployed_contract_address = str(sys.argv[2])
    # account = int(sys.argv[3])
    contract = contractClass()
    app.run_server(debug=True, port=80)
    # except IndexError:
    #     print("ERROR: MISSING ARGUMENTS")
    #     print("Usage: ./main.py {IP address:port} {Contract address} {Account index}")
