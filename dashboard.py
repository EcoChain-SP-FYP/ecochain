# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from random import randint
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
from collections import deque
from datetime import datetime
import pandas as pd
import time
import random


app = dash.Dash(__name__)

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

mlvl =[]
times = []

max_length = 10

times = deque(maxlen=max_length)
mlvl = deque(maxlen=max_length)

app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-graph'),
        dcc.Interval(
            id='interval-component',
            interval=10*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


def update_obd_values():

    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    #current_time = now.strftime("%H:%M:%S")
    times.append(current_time)
    mlvl.append(random.randrange(260,520))

    return times, mlvl


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_scatter(interval):

    update_obd_values()
    print(times)
    data = go.Scatter(
    x=list(times),
    y=list(mlvl),
    name='Scatter',
    fill="tozeroy",
    fillcolor="#6897bb"
    )

    layout = go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                    yaxis=dict(range=[min(mlvl),max(mlvl)]),
                                                    margin={'l':50,'r':1,'t':45,'b':1})
    
    return dict(data=[data], layout = layout)


if __name__ == '__main__':
    app.run_server(debug=True)