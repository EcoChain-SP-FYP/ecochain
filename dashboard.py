# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import datetime
from random import randint
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import plotly.graph_objs as go
from collections import deque


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='interval-component',
            interval=10*1000 # in milliseconds
        )
    ])
)


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-graph', 'figure'),
              [Input('interval-component', 'interval')])
def update_graph_scatter(n):

    time = datetime.datetime.now()
    mlvl = randint(260,520)
    Y.append(mlvl)
    X.append(time)

    # Create the graph with subplots
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
    
    layout = plotly.graph_objs.Layout(xaxis={'type': 'date', 
                                         'tick0': x[0], 
                                         'tickmode': 'linear', 
                                         'dtick': 86400000.0 * 14}, yaxis=dict(range=[260,520]))

    return {'data': [data],'layout' : [layout] }

if __name__ == '__main__':
    app.run_server(debug=True)