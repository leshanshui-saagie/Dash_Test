import os
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id = 'my-id', value = 'init', type = 'text'),
    html.Div(id = 'my-div')
])

@app.callback(
    Output(component_id = 'my-div', component_property = 'children'),
    [Input(component_id = 'my-id', component_property = 'value')]
)

def update_output_div(input_value):
    try:
        print(os.environ['APP_URL'])
    except:
        print("Cant get pf env var")
    return 'You have input %s'%(input_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
