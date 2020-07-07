import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
app = dash.Dash(name='app1', server=server, csrf_protect=False)
# app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
# app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for Python.''')
])


if __name__ == '__main__':
    try:
        print(os.environ['APP_URL'])
    except:
        print("Cant get pf env var")
    app.run_server(port=8077)
