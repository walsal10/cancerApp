# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State

from server import app

poeple = [['Abeer Alomran ','436000978@pnu.edu.sa' ], ['Raghad Alblaihes', '436003135@pnu.edu.sa'], ['Nourah Alqahtani','436003005@pnu.edu.sa'], ['Abeer Aldweesh','434000540@pnu.edu.sa'], ['Alanoud Aldharman','436002980@pnu.edu.sa'], ['Rana Alhussain','436001978@pnu.edu.sa']]
# Create app layout
layout = html.Div(children=[
    dcc.Location(id='abutus', refresh=True),
    dcc.Location(id='url_login2', refresh=True),
    html.Div(
        className="container",
        children=[
            html.Div(
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="ten columns",
                            children=[
                                html.Br(),
                                #html.Div('User disconnected - Please login to view the success screen again'),
                            ]
                        ),
                        html.Div(
                            className="two columns",
                            # children=html.A(html.Button('LogOut'), href='/')
                            children=[
                                html.Br(),
                                html.Button(id='back-button1', children='Go back', n_clicks=0)
                            ]
                            
                            
                            
                            
                            
                            
                        ),
                        dcc.Markdown('''
                        


## Contact us:
If you have any questions or comments you would like to share with us, please give us some of your time to do so, so that we can serve you better, please send a message by e-mail.''', style={'color': 'darkslategray'}),                        
 html.Div(
        className="trend",
        children=[
            html.Ul(id='my-list', children=[html.Li(i[0] +':'+'\t'+ str(i[1]))  for i in poeple], style={'padding-top': '2%', 'color': 'darkslategray'})
        ],
    ),
                        html.Br(),
                        html.Div('''Supervisor:''', id='h1', style={'color': 'green' , 'font-weight': '600'}),
                        html.Div('''Dr. Nithya Rekha Sivakumar''', id='h1', style={'color': 'black' , 'font-weight': '600'}),
                        html.Div('''NRRaveendiran@pnu.edu.sa''', id='h1', style={'color': 'darkslategray' , 'font-weight': '600'}),
                         html.Div('''Saudi Arabia ,Riyadh''', id='h1', style={'float': 'right', 'color': 'darkslategray' })
                    ]
                )
            )
        ]
    )
])
layout2 ="<div><p>hellow world </p>"
# Create callbacks
@app.callback(Output('url_login2', 'pathname'),
              [Input('back-button1', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'
