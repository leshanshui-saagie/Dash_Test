import dash
import dash_core_components
import dash_html_components
import numpy
import plotly.graph_objs as go
import flask


t = 20
x = numpy.linspace(0, 2 * numpy.pi, 100)
y = 10 * 2 * numpy.cos(t)

server = flask.Flask(__name__) # define flask app.server
app = dash.Dash(__name__, server=server) # call flask server

app.scripts.config.serve_locally = True # Debug use
app.css.config.serve_locally = True # Debug use
app.config.suppress_callback_exceptions = True # Debug use

app.layout = dash_html_components.Div(children=[
    dash_html_components.H1(children='Testme'),
    dash_core_components.Graph(
        id='curve', 
        figure={'data': [{'x': x, 'y': y, 'type': 'Scatter', 'name': 'Testme'},],
                'layout': {'title': 'Test Curve'} 
                })
    ])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8051)

    


