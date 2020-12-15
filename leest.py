
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:36:24 2020

@author: Programmer
"""

import dash
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']
app = dash.Dash('SimpleDashboard',external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets])
server = app.server



data={'a':'10px'}    
datas={'a':'15px'}  
datass={'a':'0px'}
carding={'ml':'15px','fs':'16px','mt':'5px'}
carding1={'ml':'15px','fs':'28px','mt':'-20px'}
inp_style={'width':'5px','height':'5px'}
PROJ_LOGO = "assets/filter.png"
PROJ_LOGO1="assets/ansl1.png"
PROJ_LOGO2="assets/ansl2.png"
PROJ_LOGO3="assets/ansl3.png"

###########################################################################
#|||||||||||||||||||| Two Site Bar Figure Data |||||||||||||||||||||||||||#
###########################################################################


def data_figure2(x1=None,y1=None,x2=None,y2=None,labels=None):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x1,
                y=y1,
                name=labels[0],
                marker_color="rgba(0, 153, 153,0.05)",
                marker_line_color='#00ffff',
                marker_line_width=2,
                opacity=1 ,
                width=[15.8,15.8,15.8,15.8,15.8]                                             
                                 )
              )

    fig.add_trace(go.Bar(x=x2,
                y=y2,
                name=labels[1],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='gold',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))


    fig.update_layout(
      xaxis_tickfont_size=14,
      showlegend=True,
      plot_bgcolor='#3d3d5c',
      paper_bgcolor='#3d3d5c',
#       paper_size='',
      margin={'l': 35, 'b': 28, 't': 0, 'r': 20},
      yaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
        gridcolor= "#47476b",
        zerolinecolor= "#3d3d5c",
        zeroline= False,
    ),
    xaxis=dict(
    gridcolor="#47476b",
     zerolinecolor= "#3d3d5c"
    ),
    legend=dict(
        x=-0.03,
        y=1.0,
       bgcolor='rgba(0,255,255,0)'
    ),
#     mode='markers',
    font={
                                        'color':'white'
                                        },
#     barmode='group',
    bargap=0, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    uniformtext_minsize=8,
    uniformtext_mode='hide'
    )
    return fig



###########################################################################
#|||||||||||||||||||| Three Site Bar Figure Data |||||||||||||||||||||||||#
###########################################################################

def data_figure3(x1=None,y1=None,x2=None,y2=None,x3=None,y3=None,labels=None):
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=x1,
                y=y1,
                name=labels[0],
         marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='#00ffff',
                                 marker_line_width=2,
                                 opacity=1       ,
                                  width=[15.8,15.8,15.8,15.8,15.8]))
    fig1.add_trace(go.Bar(x=x2,
                y=y2,
                name=labels[1],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='gold',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig1.add_trace(go.Bar(x=x3,
                y=y3,
                name=labels[2],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='white',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig1.update_layout(
      xaxis_tickfont_size=14,
      showlegend=True,
      plot_bgcolor='#3d3d5c',
      paper_bgcolor='#3d3d5c',
#       paper_size='',
      margin={'l': 35, 'b': 28, 't': 0, 'r': 20},
      yaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
        gridcolor= "#47476b",
        zerolinecolor= "#3d3d5c",
        zeroline= False,
    ),
    xaxis=dict(
    gridcolor="#47476b",
     zerolinecolor= "#3d3d5c"
    ),
    legend=dict(
        x=-0.03,
        y=1.0,
       bgcolor='rgba(0,255,255,0)'
    ),
#     mode='markers',
    font={
                                        'color':'white'
                                        },
#     barmode='group',
    bargap=0, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    uniformtext_minsize=8,
    uniformtext_mode='hide'
    )
    return fig1


###########################################################################
#|||||||||||||||||||| Four Site Bar Figure Data |||||||||||||||||||||||||#
###########################################################################
def data_figure4(x1=None,y1=None,x2=None,y2=None,x3=None,y3=None,x4=None,y4=None,labels=None):
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=x1,
                y=y1,
                name=labels[0],
         marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='#00ffff',
                                 marker_line_width=2,
                                 opacity=1,
                                  width=[15.8,15.8,15.8,15.8,15.8]))
    fig2.add_trace(go.Bar(x=x2,
                y=y2,
                name=labels[1],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='gold',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig2.add_trace(go.Bar(x=x3,
                y=y3,
                name=labels[2],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='white',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig2.add_trace(go.Bar(x=x4,
                y=y4,
                name=labels[3],
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='orange',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))


    fig2.update_layout(
      xaxis_tickfont_size=14,
      showlegend=True,
      plot_bgcolor='#3d3d5c',
      paper_bgcolor='#3d3d5c',
#       paper_size='',
      margin={'l': 35, 'b': 28, 't': 0, 'r': 20},
      yaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
        gridcolor= "#47476b",
        zerolinecolor= "#3d3d5c",
        zeroline= False,
    ),
    xaxis=dict(
    gridcolor="#47476b",
     zerolinecolor= "#3d3d5c"
    ),
    legend=dict(
        x=-0.03,
        y=1.0,
       bgcolor='rgba(0,255,255,0)'
    ),
#     mode='markers',
    font={
                                        'color':'white'
                                        },
#     barmode='group',
    bargap=0, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    uniformtext_minsize=8,
    uniformtext_mode='hide'
    )
    return fig2


###########################################################################
#|||||||||||||||||||| Five Site Bar Figure Data ||||||||||||||||||||||||||#
###########################################################################
def data_figure5(x=None,y=None,labels=None):
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=np.random.randint(20,1000,10).tolist(),
                y=['3.0','2.0','4.5','3.9','5.0'],
                name='Ali Express',
         marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='#00ffff',
                                 marker_line_width=2,
                                 opacity=1     ,
                                  width=[15.8,15.8,15.8,15.8,15.8]))
    fig3.add_trace(go.Bar(x=np.random.randint(20,1000,10).tolist(),
                y=['5.0','3.9','2.5','4.9','4.0','5.0'],
                name='Amazon',
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='gold',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig3.add_trace(go.Bar(x=np.random.randint(20,1000,10).tolist(),
                y=['2.0','4.9','3.5','3.9','5.0','4.7'],
                name='Ali Baba',
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='white',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig3.add_trace(go.Bar(x=np.random.randint(20,1000,10).tolist(),
                y=['4.0','2.9','4.5','2.9','4.0','4.9'],
                name='Flikpart',
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='orange',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))
    fig3.add_trace(go.Bar(x=np.random.randint(20,1000,10).tolist(),
                y=['5.0','4.9','1.5','4.9','3..7','5.0'],
                name='Daraz',
                     marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='green',
                                 marker_line_width=2,
                                  width=[15.8,15.8,15.8,15.8,15.8]
                ))

    fig3.update_layout(
      xaxis_tickfont_size=14,
      showlegend=True,
      plot_bgcolor='#3d3d5c',
      paper_bgcolor='#3d3d5c',
#       paper_size='',
      margin={'l': 35, 'b': 28, 't': 0, 'r': 20},
      yaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
        gridcolor= "#47476b",
        zerolinecolor= "#3d3d5c",
        zeroline= False,
    ),
    xaxis=dict(
    gridcolor="#47476b",
     zerolinecolor= "#3d3d5c"
    ),
    legend=dict(
        x=-0.03,
        y=1.0,
       bgcolor='rgba(0,255,255,0)'
    ),
#     mode='markers',
    font={
                                        'color':'white'
                                        },
#     barmode='group',
    bargap=0, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    uniformtext_minsize=8,
    uniformtext_mode='hide'
    )
    return fig3

###########################################################################
###############################---CSS---###################################
###########################################################################


container= {
    'display':'grid',
    'grid-template-columns':'repeat(3, 1fr)',
    'grid-template-rows':'repeat(3, minmax(100px, auto))',
    'grid-padding': '1em',
    'margin-top':'2rem',
    'margin-left':'3rem'
}

#placeholder layout
placeholder = {
    'background': "#eee",
    'border-style':'solid',
    'border-size':'0.5em',
    'border-color':'#ddd'
}

input_={'width':'10px','height':'10px'}
#Genrating Server 
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


#########################################################################
###################-------Navbar Starting Here-----######################
#########################################################################

dropdown= dcc.Dropdown(id='ddn',
                    options=[
                          {'label':'Amazon','value':'az'},
                          {'label':'Alibaba','value':'ab'},
                          {'label':'Flikpart','value':'fp'},
                          {'label':'Daraz','value':'dz'}],
                            value=['az'],
                            multi=True,
                            disabled=False,
                            placeholder='select site for data analysis',
                            className='drop-style',
                            
                           
                      )

#Navbar Body
navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PROJ_LOGO, height="30px",className='logo',id='_sidebar')),
                    dbc.Col(dbc.NavbarBrand("Buying Automizer", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
                  

        ),
         
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse([dropdown, html.Img(src='assets/anlss2.png',className='main_logo',height="30px")],id="navbar-collapse", navbar=True,className='drop-style'
                     ,style={'width':'10rem'}),
      
                            
                                
        ]
    ,
    color="dark",
    dark=True,
    style={'position':'fixed','width':'100%','z-index':'1000'},
   
)





#########################-------Navbar End-----############################
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
###################------Sidebar Starting Here-----########################


def side_bar():
        div=html.Nav([
        
            html.Ul([  
                html.Li([html.Br(),
                html.A(children=[
                        html.I('BA',className=" text-light font-weight-bold ")
                                ],style={'margin-left':'23.5px'}
                      )                 
                    ]),
                html.Li([
                    html.Hr(style={'width':'40px',
                                   'margin-left':'-1px',
                                   'border-top': '1px solid white'},
                            )
                ],className='container'),
            
                
                 html.Li([
                    html.Div(
                        
                        dcc.RadioItems(
                            id='realid',
                            options=[
                                {"label": "firstss", "value": 1},                             
                                {"label": "firstss", "value": 2}, 
                               
                                ],
                           inputStyle=input_,
                            value=1
                            ),id='checkout'
                        ),
                     ],className="",id='side-chart'),
                 
                  html.A(href="#",
                            children=[
                        html.Img(src='assets/anlss1.png',className='logo1'),
                        html.Span([""],className='nav-text') 
                            ],
                    
                    
                    ),
               
                  html.A(href="#",
                            children=[
                        html.Img(src='assets/help.png',className='logo3'),
                        html.Span([""],className='nav-text') 
                            ],
                    
                    
                    ),
                
             
               
                 
                    html.A(href="#",
                            children=[
                        html.Img(src='assets/real_filter.png',className='logo5'),
                        html.Span([""],className='nav-text') 
                            ],
                    
                    id='filter_'
                    ),
                  
               
          
      

               
                
                
                
                ])
            ],className="main-menu")
        
        return div



#####################-----Sidebar Body End-------###########################
#//////////////////////////////////////////////////////////////////////////# 
#//////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////#
#############------Single Website Handler Function Statrting-----###########


def show_data(quality_x1=None,
              quality_y1=None,
              products_count1=None,
              total_response1=None,
              avg_rating1=None,
              avg_price1=None,
              avgprice_x1=None,
              avgprice_y1=None,
              positive_reviews1=None,
              negative_reviews1=None,
              labels1=None):
    data=html.Div([

        
###########################################################################
##########################--- Graph Body-----##############################
###########################################################################




    dbc.CardDeck([   
        dbc.Card([html.Div(['Product Qualtiy'],style={'margin-left':'1rem',
                                                         'font-size':'25px'}
                           ,className=''),
           
                dcc.Graph(id='nice0',
                         figure={
                             'data':[go.Scatter(x=quality_x1,y=quality_y1
                                    ,name=labels1,line=dict(color='#ff33ff')),
                                     
                                    
                                     ]
                            , 'layout':{'showlegend':True,
                                     'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 35, 'b': 45, 't': 5, 'r': 25},
                                    'legend':{'x': 0, 'y': 1
                                              ,'bgcolor':'rgba(0,24,23,0)'},
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
      
          } ,
                                    
                         },className='styling1 text-light')
            ],id='styling5')
      ]),
        
    
    
    
###########################---Graph Body End---############################
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
############################----Cards Body------###########################   
    
      dbc.CardDeck([
        dbc.Card([
            dbc.CardBody([
                html.P(['Products'],className='text-right text-set '),
                dbc.Row([
                dbc.Col([
                html.Img(src='assets/product.png',className='img-style '),
              
                    html.H4(str(products_count1)+'P', className="card-title text-right show",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                    html.H6([labels1],className='ae')
                    ])
                    ])
                ]),
             dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'}),
                                     "Products Quantity "],style={'border':'white'})],className='card-style '),
            dbc.Card([
            dbc.CardBody([
                  html.P(['Count'],className='text-right text-set'),
                 html.Img(src='assets/total_count.png',className='img-style'),
                    html.H4(str(total_response1)+'C', className="card-title text-right show",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                    html.H6([labels1],className='ae')
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"People Give Feedback"],style={'border':'white'})],className='card-style')
           
         
       
           , dbc.Card([
            dbc.CardBody([
                  html.P(['Rating'],className='text-right text-set'),
                    html.Img(src='assets/real_star.png',className='img-style'),
                    html.H4(str(np.round(quality_y1.mean(),2))+'R', className="card-title text-right show",
                            style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                    html.H6([labels1],className='ae')
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"Best Average Rating "],style={'border':'white'})],className='card-style'),
            
         
         
         
            dbc.Card([
            dbc.CardBody([
                  html.P(['Price'],className='text-right text-set'),
                   html.Img(src='assets/price.png',className='img-style'),
                    html.H4(str(np.round(avg_price1.mean()*20,2))+'$', className="card-title text-right show",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
              html.H6([labels1],className='ae')
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"Best Average Price",
                                     ],style={'border':'white'})],className='card-style'),
         
    ],className='card-setting '),
     

 html.Div([
    dbc.CardDeck([   
        dbc.Card([
            html.P(['Average Prices'],style={'margin-left':carding['ml']
                                                       ,'margin-top':carding['mt']}),
           
                    dcc.Graph(id='nice0',
                         figure={
                             'data':[go.Scatter(x=quality_x1, y=avg_price1, fill='tozeroy',mode=None,
                                                fillcolor='rgba(147, 55, 203,0.07)',name=labels1),
                                     ]
                            ,  'layout':{'showlegend':True,
                                   'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 25, 'b': 45, 't': 10, 'r': 20},
                                    'legend':{'x': 0, 'y': 1,'bgcolor':'rgba(0,24,23,0)'},
                                    
                                    'mode':'markers',
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c",
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
                                    } 
                         },style={'height':'19rem'})
            
        ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                 'font-size':carding['fs']},
            className='text-light'),
        html.Br(),html.Br(),html.Br(),
         dbc.Card([
            html.P(['Price & Quality'],style={'margin-left':carding['ml']
                                              ,'margin-top':carding['mt']}),
                    dcc.Graph(id='nice2',
                         figure={
                             'data':[go.Bar(
                                 x=avg_price1,
                                 y=quality_y1,
                                 name=labels1,
                                 marker_color="rgba(0, 153, 153,0.05)",
                                 marker_line_color='#00ffff',
                                 marker_line_width=2,
                                 opacity=1
                                 )]
                            , 'layout':{'showlegend':True,
                                   'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 25, 'b': 45, 't': 0, 'r': 0},
                                    'legend':{'x': 0, 'y': 1,'bgcolor':'rgba(0,24,23,0)'},
                                    
                                    'mode':'markers',
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c",
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
                                    }   
                         },style={'height':'19rem'})                                
            ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                     'font-size':carding['fs']},
              className='text-light'),
                      html.Br(),html.Br(),html.Br(),
        dbc.Card([
            html.P(['Positive & Negative Reviews'],style={'margin-left':carding['ml']
                                                          ,'margin-top':carding['mt']}),
             

                   dcc.Graph(id='nice1',
                         figure={
                             'data':[go.Pie(labels=['Positive','Negative'],
                                            values=[positive_reviews1,negative_reviews1],hole=.6,
                                            marker=dict(colors=[' #1ac6ff','darkorange']),
                                            rotation=120,
                                            text=[labels1,labels1]
                                            )],
                             'layout':{
                                 
                                 'showlegend':True,
                                   'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 25, 'b': 45, 't': 0, 'r': 0},
                                    'legend':{
                                        'x': -0.2, 'y': 1,'bgcolor':'rgba(0,24,23,0)'
                                        
                                        },
                                   "annotations":[dict(text='%', x=0.5, y=0.5, font_size=50, showarrow=False)],
                                    'mode':'markers',
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c",
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
                                    } 
                             
                             }   
                         ,style={'height':'19rem'}),
               
                
        ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                 'font-size':carding['fs']},
            className=' text-light'),
       
        ],className='card-setting')
    ]),html.Br(),html.Br(),html.Br(),
###########################################################################
########################----Cards body End----#############################
###########################################################################




     
    ],style={'margin-right':'0rem',
             'margin-top':'0rem'})


    return data


###############---Single Websites Handler Funcion Ended-----###############
#/////////////////////////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////#
###############---Two Websites Handler Funcion Starting-----###############



def show_data2(quality_x1=None,
               quality_y1=None,
               products_count1=None,
               total_response1=None,
               avg_rating1=None,
               avg_price1=None,
               avgprice_x1=None,
               avgprice_y1=None,
               positive_reviews1=None,
               negative_reviews1=None,
               labels1=None,
               
               quality_x2=None,
               quality_y2=None,
               products_count2=None,
               total_response2=None,
               avg_rating2=None,
               avg_price2=None,
               avgprice_x2=None,
               avgprice_y2=None,
               positive_reviews2=None,
               negative_reviews2=None,
               labels2=None,
               ):
    data=html.Div([
        
        
        
###########################################################################
##########################--- Graph Body-----##############################
###########################################################################



    dbc.CardDeck([   
        dbc.Card([html.Div(['Product Qualtiy'],style={'margin-left':'1rem',
                                                         'font-size':'25px'}
                           ,className=''),
           
                dcc.Graph(id='nice0',
                         figure={
                             'data':[go.Scatter(x=quality_x1,y=quality_y1
                                    ,name=labels1,line=dict(color='#ff33ff')),
                                     go.Scatter(x=quality_x1,y=quality_y2
                                    ,name=labels2,line=dict(color='white')),
                                    
                                     ]
                            , 'layout':{'showlegend':True,
                                     'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 35, 'b': 25, 't': 0, 'r': 20},
                                    'legend':{'x': 0, 'y': 1,'bgcolor':'rgba(0,24,23,0)'},
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
      
          } ,
                                    
                         },className='styling1 text-light')
            ],id='styling5')
      ]),
        
    
    
###########################---Graph Body End---############################
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
############################----Cards Body------###########################         
         


      dbc.CardDeck([
        dbc.Card([
            dbc.CardBody([
                html.P(['Products'],className='text-right text-set'),
                html.Img(src='assets/product.png',className='img-style'),
                    html.H4(products_count1, className="card-title text-right ",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                     html.H4(products_count2, className="card-title text-right two",
                             style={'margin-bottom':'-30px','margin-top':'0.3rem'}),
                   html.Div([
                       html.P(labels1,className='first'),
                       html.P(labels2,className='second')
                       ],className='az')
                ]),
             dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'}),
                                     "Products Quantity "],style={'border':'white'})],className='card-style'),
            dbc.Card([
            dbc.CardBody([
                  html.P(['Count'],className='text-right text-set'),
                 html.Img(src='assets/total_count.png',className='img-style'),
                    html.H4(np.round(total_response1,2), className="card-title text-right ",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                    html.H4(np.round(total_response2,2), className="card-title text-right two",
                             style={'margin-bottom':'-30px','margin-top':'0.3rem'}),
                      html.Div([
                       html.P(labels1,className='first'),
                       html.P(labels2,className='second')
                       ],className='az')
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"People Give Feedback"],style={'border':'white'})],className='card-style')
           
         
       
           , dbc.Card([
            dbc.CardBody([
                  html.P(['Rating'],className='text-right text-set'),
                    html.Img(src='assets/real_star.png',className='img-style'),
                    html.H4(np.round(avg_rating1,2), className="card-title text-right ",
                            style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                     html.H4(np.round(avg_rating2,2), className="card-title text-right two",
                            style={'margin-bottom':'-30px','margin-top':'0.3rem'}),
                     html.Div([
                       html.P(labels1,className='first'),
                       html.P(labels2,className='second')
                       ],className='az')
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"Best Average Rating "],style={'border':'white'})],className='card-style'),
            
         
         
         
            dbc.Card([
            dbc.CardBody([
                  html.P(['Price'],className='text-right text-set'),
                   html.Img(src='assets/price.png',className='img-style'),
                    html.H4(str(np.round(avg_price1.mean()*20,2))+'$', className="card-title text-right ",
                             style={'margin-bottom':'-10px','margin-top':'-2rem'}),
                     html.H4(str(np.round(avg_price2.mean()*20,2))+'$', className="card-title text-right two",
                             style={'margin-bottom':'-30px','margin-top':'0.3rem'}),
                       html.Div([
                           html.P(labels1,className='first'),
                           html.P(labels2,className='second')
                       ],className='az')
              
                ]),
            dbc.CardFooter(children=[
                html.Hr(style={'border-top': '1px solid white','margin-bottom':'8px'})
                                     ,"Best Average Price",
                                     ],style={'border':'white'})],className='card-style'),
         
    ],className='card-setting '),
     




###########################################################################
########################----Cards body End----#############################
###########################################################################




#///////////////////////////////////////////////////////////////////////



 html.Div([
    dbc.CardDeck([   
        dbc.Card([
            html.P(['Average Prices'],style={'margin-left':carding['ml']
                                                       ,'margin-top':carding['mt']}),
           
                    dcc.Graph(id='nice0',
                         figure={
                             'data':[go.Scatter(x=quality_x1, y=avg_price1, fill='tozeroy',line=dict(color='#ff33ff',width=3),name=labels1,
                                                fillcolor='rgba(147, 55, 203,0.07)',marker=dict(size=8)),
                                     go.Scatter(x=quality_x1, y=avg_price2,line=dict(color='white',width=3),name=labels2
                                                ,marker=dict(size=8),fill='tozeroy',fillcolor='rgba(147, 55, 203,0.07)')]
                            ,  'layout':{'showlegend':True,
                                   'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 25, 'b': 30, 't': 0, 'r': 20},
                                    'legend':{'x': -0.05, 'y': 1,
                                              'bgcolor':'rgba(0,24,23,0)'},
                                    
                                    'mode':'markers',
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c",
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
                                    } 
                         },style={'height':'19rem'})
            
        ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                 'font-size':carding['fs']},
            className='text-light'),
        
                 html.Br(),html.Br(),html.Br(),
                 
         dbc.Card([
            html.P(['Price & Quality'],style={'margin-left':carding['ml']
                                              ,'margin-top':carding['mt']}),
                    dcc.Graph(id='nice2',
                         figure=data_figure2(x1=avg_price1,y1=quality_y1,x2=avg_price2,y2=quality_y2,labels=[labels1,labels2])
                         ,style={'height':'19rem'})                                
            ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                     'font-size':carding['fs']},
              className='text-light'),
                     
                     
                     html.Br(),html.Br(),html.Br(),

        dbc.Card([
            html.P(['Positive & Negative Reviews'],style={'margin-left':carding['ml']
                                                          ,'margin-top':carding['mt']}),
             

                   dcc.Graph(id='nice1',
                         figure={
                             'data':[go.Pie(labels=['Positive','Negative','Positive1','Negative1'],
                                            values=[positive_reviews1,negative_reviews1,positive_reviews2,negative_reviews2],hole=.6,
                                            marker=dict(colors=[' red','green']),
                                            rotation=120,
                                            text=[labels1,labels1,labels2,labels2]
                                            ),
                                   ],
                             'layout':{
                                 
                                 'showlegend':True,
                                   'plot_bgcolor':'#3d3d5c',
                                    'paper_bgcolor':'#3d3d5c',
                                    'paper_size':'20rem',
                                    'margin':{'l': 25, 'b': 25, 't': 0, 'r': 0},
                                    'legend':{
                                        'x': -0.2, 'y': 1,'bgcolor':'rgba(0,24,23,0)'
                                        
                                        },
                                   "annotations":[dict(text='%', x=0.5, y=0.5, font_size='50', showarrow=False)],
                                    'mode':'markers',
                                    'font':{
                                        'color':'white'
                                        },
                                    "yaxis1":{
                                         "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c",
                                         "zeroline": False,
                                        },
                                    "xaxis1": {
      
                                        "gridcolor": "#47476b",
                                        "zerolinecolor": "#3d3d5c"
                                        }, 
                                    } 
                             
                             }   
                         ,style={'height':'19rem'}),
               
                
        ],style={'height':'18rem',"border":'#3d3d5c','background':'#3d3d5c',
                 'font-size':carding['fs']},
            className=' text-light'),
       
        ],className='card-setting')
    ]),
                 html.Br(),html.Br(),html.Br(),
     
    ],style={'margin-right':'0rem',
             'margin-top':'0rem'})

        

    return data



###############---Two Websites Handler Funcion Ended-----#################
#/////////////////////////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////#
##########---This is Content where our output will be show-----############



filters=html.Div([
        dbc.CardDeck([
               
           

        dbc.Card([
           

           
            dbc.CardBody([
                 html.Br(),
             html.Img(src='assets/anls3.jpg',className='logo2'),
html.Div([
             
      dbc.Col(children=[
                        dbc.Checklist(
                            id="prices",
                            options=[
                                {"label": "Low 00-30%", "value": 'low'},
                                {"label": "Normal 30-60%", "value": 'normal'},
                                {"label": "High 60-100%", "value": 'high'},
                              
                                
                                ]
                            )]),
                                 ],className='price_style'),
                    
                    html.Hr(),
#########################################################################         
#########################################################################   
#                  First Outer Div as Main Trigger                     #
#########################################################################                
#########################################################################    

        html.Div([
             
      dbc.Col(children=[
                        dbc.Checklist(
                            id="items1",
                            options=[
                                {"label": "Toys", "value": 'all_toys'},
                                {"label": "Dolls", "value": 'dolls'},
                                {"label": "Board GM", "value": 'board'},
                                {"label": "Soft Toys", "value": 'soft'},
                                {"label": "Edu Toys", "value": 'edu'},
                                
                                ]
                            )]),
                                 ],className='first_inner_collapse'),
                    
                    
                    
                
                   
#########################################################################         
#########################################################################   
#                  Second Outer Div as Main Trigger                     #
#########################################################################                
######################################################################### 
                
                html.Div([
                
           dbc.Col(children=[
                        dbc.Checklist(
                            id="items2",
                            options=[
                                {"label": "Shoes(men)", "value": 'all_shoes'},
                                {"label": "Dress", "value": 'dress'},
                                {"label": "Clogs", "value": 'clogs'},
                                {"label": "Sandals", "value": 'sandals'},
                                {"label": "Sneakers", "value": 'sneakers'},
                                ]
                            )]),
                                 ],className='second_inner_collapse'),
        
                
                
                
                
                    
#########################################################################         
#########################################################################   
#                   Third Outer Div as Main Trigger                     #
#########################################################################                
######################################################################### 
                


                html.Div([
                    
                dbc.Col(children=[
                        dbc.Checklist(
                            id="items3",
                            options=[
                                
                              {"label": "Handsfree", "value": 'all_handsfree'},
                                {"label": "In Ear (Wired)", "value": 'inearwrd'},
                                {"label": "In Ear (Wireless)", "value": 'inearwrls'},
                                {"label": "Over Ear (Wired)", "value": 'ovrearwrd'},
                                {"label": "Over Ear (wireless)", "value": 'ovrearwrls'},
                                ]
                            )])
             
              ],className='fourth_inner_collapse')  
                                 
                             
     ,    


#///////////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////////////////#
               html.Br(),
               html.Br(),
               html.Br(),
               
                ]),
        
        ])
        ])],className='filter_dealer')



content=html.Div(id='output',className='container-fluid CONTENT_STYLE')

##########-----Main Layout where all outputs digested------###########


app.layout=html.Div([     
   navbar,
   dbc.Collapse(side_bar(),id='sidebar_collapse'),
   dbc.Collapse(filters,id='filter_collapse',className='filter_style'),
   content,
],className='back-g')



###########################################################################
########################-----Main Layout End-------########################   
###########################################################################


def conditions(value_s,tys,pr):
        start=0
        end=0
        print(tys)
        print(pr)
        if tys==[] and pr==['Null','Null','Null']:
            if len(value_s)==1:                 
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset

                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')

                    print(df_ab.Rating.mean())
                    
                    return show_data(      
                                quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 
                                 )
            if len(value_s)==2:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ae':
                            vali='Ali_Express'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')
                    df_ab1=pd.read_csv(f'{real[1]}\\analysed.csv',encoding='latin')
                    df1=pd.read_csv(f'{real[1]}\\raw.csv',encoding='latin')
                    
                   
                    return show_data2(      
                                 quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
                                 quality_x2=df_ab1.Base,
                                 quality_y2=df_ab1.Rating,
                                 avg_rating2=df_ab1.Rating.mean(),
                                 avg_price2=df_ab1.Prices,
                                 avgprice_x2=df_ab1.Prices,
                                 avgprice_y2=df_ab1.Rating,
                                 products_count2=df1.shape[0],
                                 total_response2=df1.Response.sum(),
                                 labels2=real[1].replace('_',' '),
                                 positive_reviews2=df_ab1.Positive.mean(),
                                 negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
                                 
                                      
                                      )
            # if len(value_s)==3:
            #         lst=value_s
            #         real=[]
            #         for vali in lst:
            #             if vali=='az':
            #                 vali='Amazon'
            #                 real.append(vali)
            #             if vali=='ae':
            #                 vali='Ali_Express'
            #                 real.append(vali)
            #             if vali=='ab':
            #                 vali='Ali_Baba'
            #                 real.append(vali)
            #             if vali=='fp':
            #                 vali='Flikpart'
            #                 real.append(vali)
            #             if vali=='dz':
            #                 vali='Daraz'
            #                 real.append(vali)
            #         # Loading Dataset
            #         df_ab=pd.read_csv(f'E:\\{real[0]}\\analysed.csv',encoding='latin')
            #         df=pd.read_csv(f'E:\\{real[0]}\\raw.csv',encoding='latin')
            #         df_ab1=pd.read_csv(f'E:\\{real[1]}\\analysed.csv',encoding='latin')
            #         df1=pd.read_csv(f'E:\\{real[1]}\\raw.csv',encoding='latin')
            #         df_ab2=pd.read_csv(f'E:\\{real[2]}\\analysed.csv',encoding='latin')
            #         df2=pd.read_csv(f'E:\\{real[2]}\\raw.csv',encoding='latin')
                    
            #         return show_data3(      quality_x1=df_ab.Base,
            #                       quality_y1=df_ab.Rating,
            #                       avg_rating1=df_ab.Rating.mean(),
            #                       avg_price1=df_ab.Prices,
            #                       avgprice_x1=df_ab.Prices,
            #                       avgprice_y1=df_ab.Rating,
            #                       products_count1=df.shape[0],
            #                       total_response1=df.Response.sum(),
            #                       labels1=real[0].replace('_',' '),
            #                       positive_reviews1=df_ab.Positive.mean(),
            #                       negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
            #                       quality_x2=df_ab1.Base,
            #                       quality_y2=df_ab1.Rating,
            #                       avg_rating2=df_ab1.Rating.mean(),
            #                       avg_price2=df_ab1.Prices,
            #                       avgprice_x2=df_ab1.Prices,
            #                       avgprice_y2=df_ab1.Rating,
            #                       products_count2=df1.shape[0],
            #                       total_response2=df1.Response.sum(),
            #                       labels2=real[1].replace('_',' '),
            #                       positive_reviews2=df_ab1.Positive.mean(),
            #                       negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
            #                       quality_x3=df_ab2.Base,
            #                       quality_y3=df_ab2.Rating,
            #                       avg_rating3=df_ab2.Rating.mean(),
            #                       avg_price3=df_ab2.Prices,
            #                       avgprice_x3=df_ab2.Prices,
            #                       avgprice_y3=df_ab2.Rating,
            #                       products_count3=df2.shape[0],
            #                       total_response3=df2.Response.sum(),
            #                       labels3=real[2].replace('_',' '),
            #                       positive_reviews3=df_ab2.Positive.mean(),
            #                       negative_reviews3=df_ab2.Negative.mean(),
                                 
                                 
            #                       )
            # if len(value_s)==4:
            #         lst=value_s
            #         real=[]
            #         for vali in lst:
            #             if vali=='az':
            #                 vali='Amazon'
            #                 real.append(vali)
            #             if vali=='ae':
            #                 vali='Ali_Express'
            #                 real.append(vali)
            #             if vali=='ab':
            #                 vali='Ali_Baba'
            #                 real.append(vali)
            #             if vali=='fp':
            #                 vali='Flikpart'
            #                 real.append(vali)
            #             if vali=='dz':
            #                 vali='Daraz'
            #                 real.append(vali)
            #         # Loading Dataset
            #         df_ab=pd.read_csv(f'E:\\{real[0]}\\analysed.csv',encoding='latin')
            #         df=pd.read_csv(f'E:\\{real[0]}\\raw.csv',encoding='latin')
            #         df_ab1=pd.read_csv(f'E:\\{real[1]}\\analysed.csv',encoding='latin')
            #         df1=pd.read_csv(f'E:\\{real[1]}\\raw.csv',encoding='latin')
            #         df_ab2=pd.read_csv(f'E:\\{real[2]}\\analysed.csv',encoding='latin')
            #         df2=pd.read_csv(f'E:\\{real[2]}\\raw.csv',encoding='latin')
            #         df_ab3=pd.read_csv(f'E:\\{real[3]}\\analysed.csv',encoding='latin')
            #         df3=pd.read_csv(f'E:\\{real[3]}\\raw.csv',encoding='latin')
                    
                   
            #         return show_data4(      quality_x1=df_ab.Base,
            #                       quality_y1=df_ab.Rating,
            #                       avg_rating1=df_ab.Rating.mean(),
            #                       avg_price1=df_ab.Prices,
            #                       avgprice_x1=df_ab.Prices,
            #                       avgprice_y1=df_ab.Rating,
            #                       products_count1=df.shape[0],
            #                       total_response1=df.Response.sum(),
            #                       labels1=real[0].replace('_',' '),
            #                       positive_reviews1=df_ab.Positive.mean(),
            #                       negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
            #                       quality_x2=df_ab1.Base,
            #                       quality_y2=df_ab1.Rating,
            #                       avg_rating2=df_ab1.Rating.mean(),
            #                       avg_price2=df_ab1.Prices,
            #                       avgprice_x2=df_ab1.Prices,
            #                       avgprice_y2=df_ab1.Rating,
            #                       products_count2=df1.shape[0],
            #                       total_response2=df1.Response.sum(),
            #                       labels2=real[1].replace('_',' '),
            #                       positive_reviews2=df_ab1.Positive.mean(),
            #                       negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
            #                       quality_x3=df_ab2.Base,
            #                       quality_y3=df_ab2.Rating,
            #                       avg_rating3=df_ab2.Rating.mean(),
            #                       avg_price3=df_ab2.Prices,
            #                       avgprice_x3=df_ab2.Prices,
            #                       avgprice_y3=df_ab2.Rating,
            #                       products_count3=df2.shape[0],
            #                       total_response3=df2.Response.sum(),
            #                       labels3=real[2].replace('_',' '),
            #                       positive_reviews3=df_ab2.Positive.mean(),
            #                       negative_reviews3=df_ab2.Negative.mean(),
                                 
            #                       quality_x4=df_ab3.Base,
            #                       quality_y4=df_ab3.Rating,
            #                       avg_rating4=df_ab3.Rating.mean(),
            #                       avg_price4=df_ab3.Prices,
            #                       avgprice_x4=df_ab3.Prices,
            #                       avgprice_y4=df_ab3.Rating,
            #                       products_count4=df3.shape[0],
            #                       total_response4=df3.Response.sum(),
            #                       labels4=real[3].replace('_',' '),
            #                       positive_reviews4=df_ab3.Positive.mean(),
            #                       negative_reviews4=df_ab3.Negative.mean(),
                                 
            #                       )
            # if len(value_s)==5:
            #         lst=value_s
            #         real=[]
            #         for vali in lst:
            #             if vali=='az':
            #                 vali='Amazon'
            #                 real.append(vali)
            #             if vali=='ae':
            #                 vali='Ali_Express'
            #                 real.append(vali)
            #             if vali=='ab':
            #                 vali='Ali_Baba'
            #                 real.append(vali)
            #             if vali=='fp':
            #                 vali='Flikpart'
            #                 real.append(vali)
            #             if vali=='dz':
            #                 vali='Daraz'
            #                 real.append(vali)
            #         # Loading Dataset
            #         df_ab=pd.read_csv(f'E:\{real[0]}\analysed.csv')
            #         df=pd.read_csv(f'E:\{real[0]}\raw.csv')
            #         df_ab1=pd.read_csv(f'E:\{real[1]}\analysed.csv')
            #         df1=pd.read_csv(f'E:\{real[1]}\raw.csv')
            #         df_ab2=pd.read_csv(f'E:\{real[2]}\analysed.csv')
            #         df2=pd.read_csv(f'E:\{real[2]}\raw.csv')
            #         df_ab3=pd.read_csv(f'E:\{real[3]}\analysed.csv')
            #         df3=pd.read_csv(f'E:\{real[3]}\raw.csv')
            #         df_ab4=pd.read_csv(f'E:\{real[4]}\analysed.csv')
            #         df4=pd.read_csv(f'E:\{real[4]}\raw.csv')
                    
                    
                    
            #         return show_data5(  
            #                       quality_x1=df_ab.Base,
            #                       quality_y1=df_ab.Rating,
            #                       avg_rating1=df_ab.Rating.mean(),
            #                       avg_price1=df_ab.Prices,
            #                       avgprice_x1=df_ab.Prices,
            #                       avgprice_y1=df_ab.Rating,
            #                       products_count1=np.round((df_ab.Products.values[0]/df.shape[0])*df_ab.shape[0],0),
            #                       total_response1=df_ab.Response.values[0],
            #                       labels1=real[0].replace('_',' '),
            #                       positive_reviews1=df.Positive,
            #                       negative_reviews1=df.Negative,
                                 
                                 
            #                       quality_x2=df_ab1.Base,
            #                       quality_y2=df_ab1.Rating,
            #                       avg_rating2=df_ab1.Rating.mean(),
            #                       avg_price2=df_ab1.Prices,
            #                       avgprice_x2=df_ab1.Prices,
            #                       avgprice_y2=df_ab1.Rating,
            #                       products_count2=np.round((df_ab1.Products.values[0]/df1.shape[0])*df_ab1.shape[0],0),
            #                       total_response2=df_ab1.Response.values[0],
            #                       labels2=real[1].replace('_',' '),
            #                       positive_reviews2=df.Positive,
            #                       negative_reviews2=df.Negative,
                                 
            #                       quality_x3=df_ab2.Base,
            #                       quality_y3=df_ab2.Rating,
            #                       avg_rating3=df_ab2.Rating.mean(),
            #                       avg_price3=df_ab2.Prices,
            #                       avgprice_x3=df_ab2.Prices,
            #                       avgprice_y3=df_ab2.Rating,
            #                       products_count3=np.round((df_ab2.Products.values[0]/df2.shape[0])*df_ab2.shape[0],0),
            #                       total_response3=df_ab2.Response.values[0],
            #                       labels3=real[2].replace('_',' '),
            #                       positive_reviews3=df.Positive,
            #                       negative_reviews3=df.Negative,
                                 
            #                       quality_x4=df_ab3.Base,
            #                       quality_y4=df_ab3.Rating,
            #                       avg_rating4=df_ab3.Rating.mean(),
            #                       avg_price4=df_ab3.Prices,
            #                       avgprice_x4=df_ab3.Prices,
            #                       avgprice_y4=df_ab3.Rating,
            #                       products_count4=np.round((df_ab3.Products.values[0]/df3.shape[0])*df_ab3.shape[0],0),
            #                       total_response4=df_ab3.Response.values[0],
            #                       labels4=real[3].replace('_',' '),
            #                       positive_reviews4=df.Positive,
            #                       negative_reviews4=df.Negative,
                                 
            #                       quality_x5=df_ab4.Base,
            #                       quality_y5=df_ab4.Rating,
            #                       avg_rating5=df_ab4.Rating.mean(),
            #                       avg_price5=df_ab4.Prices,
            #                       avgprice_x5=df_ab4.Prices,
            #                       avgprice_y5=df_ab4.Rating,
            #                       products_count5=np.round((df_ab4.Products.values[0]/df4.shape[0])*df_ab4.shape[0],0),
            #                       total_response5=df_ab4.Response.values[0],
            #                       labels5=real[4].replace('_',' '),
            #                       positive_reviews5=df.Positive,
            #                       negative_reviews5=df.Negative,
            #                       )
                
        if tys!=[]  and pr==['Null','Null','Null']:
                value=''
                if len(value_s)==1:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)           
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')

                    
                    print(df_ab.Rating.mean())

                    df_ab=df_ab[(df_ab.cat.isin(tys))]
                    df=df[(df.cat.isin(tys))]

                    return show_data(      

                                 quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),

                                 )
                if len(value_s)==2:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ae':
                            vali='Ali_Express'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')
                    df_ab1=pd.read_csv(f'{real[1]}\\analysed.csv',encoding='latin')
                    df1=pd.read_csv(f'{real[1]}\\raw.csv',encoding='latin')
                    
                    
                    df_ab=df_ab[df_ab.cat.isin(tys)]
                    df_ab1=df_ab1[df_ab1.cat.isin(tys)]
                    df=df[(df.cat.isin(tys))]
                    df1=df1[(df1.cat.isin(tys))]
                    return show_data2(      
                                 quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
                                 quality_x2=df_ab1.Base,
                                 quality_y2=df_ab1.Rating,
                                 avg_rating2=df_ab1.Rating.mean(),
                                 avg_price2=df_ab1.Prices,
                                 avgprice_x2=df_ab1.Prices,
                                 avgprice_y2=df_ab1.Rating,
                                products_count2=df1.shape[0],
                                 total_response2=df1.Response.sum(),
                                 labels2=real[1].replace('_',' '),
                                 positive_reviews2=df_ab1.Positive.mean(),
                                 negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
                                      
                                      )
                # if len(value_s)==3:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\\{real[0]}\\Datasets\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\\{real[0]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\raw.csv',encoding='latin')
            
                    
                    
                #     df_ab=df_ab[df_ab.cat.isin(tys)]
                #     df_ab1=df_ab1[df_ab1.cat.isin(tys)]
                #     df_ab2=df_ab2[df_ab2.cat.isin(tys)]
                    
                #     df=df[(df.cat.isin(tys))]
                #     df1=df1[(df1.cat.isin(tys))]
                #     df2=df2[(df2.cat.isin(tys))]
                #     return show_data3(      quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df1.shape[0],
                #                  total_response2=df1.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab1.Positive.mean(),
                #                  negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                                 
                                 
                #                  )
                # if len(value_s)==4:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\\{real[0]}\\Datasets\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\\{real[0]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\Datasets\raw.csv',encoding='latin')
                #     df_ab3=pd.read_csv(f'E:\\{real[3]}\\Datasets\\analysed.csv',encoding='latin')
                #     df3=pd.read_csv(f'E:\\{real[3]}\\Datasets\\raw.csv',encoding='latin')
            

                #     df_ab=df_ab[df_ab.cat.isin(tys)]
                #     df_ab1=df_ab1[df_ab1.cat.isin(tys)]
                #     df_ab2=df_ab2[df_ab2.cat.isin(tys)]
                #     df_ab3=df_ab3[df_ab3.cat.isin(tys)]
                    
                #     df=df[(df.cat.isin(tys))]
                #     df1=df1[(df1.cat.isin(tys))]
                #     df2=df2[(df2.cat.isin(tys))]
                #     df3=df3[(df3.cat.isin(tys))]
                #     return show_data4(      
                #                  quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df.shape[0],
                #                  total_response2=df.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab.Positive.mean(),
                #                  negative_reviews2=df_ab.Negative.mean(),
                                 
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                                 
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=df3.shape[0],
                #                  total_response4=df3.Response.sum(),
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df_ab3.Positive.mean(),
                #                  negative_reviews4=df_ab3.Negative.mean(),
                                 
                #                  )
                # if len(value_s)==5:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\{real[0]}\Datasets\analysed.csv')
                #     df=pd.read_csv(f'E:\{real[0]}\Datasets\raw.csv')
                #     df_ab1=pd.read_csv(f'E:\{real[1]}\Datasets\analysed.csv')
                #     df1=pd.read_csv(f'E:\{real[1]}\Datasets\raw.csv')
                #     df_ab2=pd.read_csv(f'E:\{real[2]}\Datasets\analysed.csv')
                #     df2=pd.read_csv(f'E:\{real[2]}\Datasets\raw.csv')
                #     df_ab3=pd.read_csv(f'E:\{real[3]}\Datasets\analysed.csv')
                #     df3=pd.read_csv(f'E:\{real[3]}\Datasets\raw.csv')
                #     df_ab4=pd.read_csv(f'E:\{real[4]}\Datasets\analysed.csv')
                #     df4=pd.read_csv(f'E:\{real[4]}\Datasets\raw.csv')
                    
                #     df_ab=df_ab[df_ab.cat.isin(tys)]
                #     df_ab1=df_ab1[df_ab1.cat.isin(tys)]
                #     df_ab2=df_ab2[df_ab2.cat.isin(tys)]
                #     df_ab3=df_ab3[df_ab3.cat.isin(tys)]
                #     df_ab4=df_ab4[df_ab4.cat.isin(tys)]
                    
                #     df=df[(df.cat.isin(tys))]
                #     df1=df1[(df1.cat.isin(tys))]
                #     df2=df2[(df2.cat.isin(tys))]
                #     df3=df3[(df3.cat.isin(tys))]
                #     df4=df4[(df4.cat.isin(tys))]
                #     return show_data5(  
                #                  quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=np.round((df_ab.Products.values[0]/df.shape[0])*df_ab.shape[0],0),
                #                  total_response1=df_ab.Response.values[0],
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df.Positive,
                #                  negative_reviews1=df.Negative,
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=np.round((df_ab1.Products.values[0]/df1.shape[0])*df_ab1.shape[0],0),
                #                  total_response2=df_ab1.Response.values[0],
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df.Positive,
                #                  negative_reviews2=df.Negative,
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=np.round((df_ab2.Products.values[0]/df2.shape[0])*df_ab2.shape[0],0),
                #                  total_response3=df_ab2.Response.values[0],
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df.Positive,
                #                  negative_reviews3=df.Negative,
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=np.round((df_ab3.Products.values[0]/df3.shape[0])*df_ab3.shape[0],0),
                #                  total_response4=df_ab3.Response.values[0],
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df.Positive,
                #                  negative_reviews4=df.Negative,
                                 
                                 
                #                  quality_x5=df_ab4.Base,
                #                  quality_y5=df_ab4.Rating,
                #                  avg_rating5=df_ab4.Rating.mean(),
                #                  avg_price5=df_ab4.Prices,
                #                  avgprice_x5=df_ab4.Prices,
                #                  avgprice_y5=df_ab4.Rating,
                #                  products_count5=np.round((df_ab4.Products.values[0]/df4.shape[0])*df_ab4.shape[0],0),
                #                  total_response5=df_ab4.Response.values[0],
                #                  labels5=real[4].replace('_',' '),
                #                  positive_reviews5=df.Positive,
                #                  negative_reviews5=df.Negative,
                                 
                #                  )
                
        if tys==[]  and pr!=['Null','Null','Null']:
                value=''
                if len(value_s)==1:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')


                    if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*pr[0]
                    if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*pr[0]
                    if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.6
                        end=df_ab.Prices.max()
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*0.6
                    if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*0.9
                    if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:                  
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()    
                    
                    df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end)]
                    return show_data(      
                                quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 )
                if len(value_s)==2:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ae':
                            vali='Ali_Express'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')
                    df_ab1=pd.read_csv(f'{real[1]}\\analysed.csv',encoding='latin')
                    df1=pd.read_csv(f'{real[1]}\\raw.csv',encoding='latin')
                    
                    if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*pr[0]
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()*pr[0]
                        
                    
                    if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*pr[0]
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()*pr[0]
                       
                    if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.6
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.max()*0.6
                        end1=df_ab1.Prices.max()
                      
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*0.6
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()*0.6
                     
                    if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*0.9
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()*0.9
                       
                    if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()
                       
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()
                       
                  
                    df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end)]
                    df_ab1=df_ab1[(df_ab1.Prices>=start1) & (df_ab1.Prices<=end1)]
                    return show_data2(      
                        
                                 quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 
                                 quality_x2=df_ab1.Base,
                                 quality_y2=df_ab1.Rating,
                                 avg_rating2=df_ab1.Rating.mean(),
                                 avg_price2=df_ab1.Prices,
                                 avgprice_x2=df_ab1.Prices,
                                 avgprice_y2=df_ab1.Rating,
                                 products_count2=df1.shape[0],
                                 total_response2=df1.Response.sum(),
                                 labels2=real[1].replace('_',' '),
                                 positive_reviews2=df_ab1.Positive.mean(),
                                 negative_reviews2=df_ab1.Negative.mean(),
                                 
                                      
                                      )
                # if len(value_s)==3:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\\{real[0]}\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\\{real[0]}\\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\\raw.csv',encoding='latin')
                  
                    
                #     if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*pr[0]
                    
                    
                #     if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*pr[0]
               
                #     if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #         print('-----------------')
                #         start=df_ab.Prices.max()*0.6
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.6
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.6
                #         end2=df_ab2.Prices.max()
               
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*0.6
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*0.6
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*0.6
                      
                #     if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*0.9
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*0.9
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*0.9
              
                #     if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()
                   
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()
      

           
                    
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end)]
                #     df_ab1=df_ab1[(df_ab1.Prices>=start1) & (df_ab1.Prices<=end1)]
                #     df_ab2=df_ab2[(df_ab2.Prices>=start2) & (df_ab2.Prices<=end2)]
                #     return show_data3(      quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df1.shape[0],
                #                  total_response2=df1.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab1.Positive.mean(),
                #                  negative_reviews2=df_ab1.Negative.mean(),
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                #                  )
                # if len(value_s)==4:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\{real[0]}\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\{real[0]}\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\\raw.csv',encoding='latin')
                #     df_ab3=pd.read_csv(f'E:\\{real[3]}\\analysed.csv',encoding='latin')
                #     df3=pd.read_csv(f'E:\\{real[3]}\\raw.csv',encoding='latin')                    
                  
                    
                    
                #     if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*pr[0]
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()*pr[0]
                 
                    
                #     if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*pr[0]
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()*pr[0]
          
                #     if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.6
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.6
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.6
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.max()*0.6
                #         end3=df_ab3.Prices.max()
              
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*0.6
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*0.6
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*0.6
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()*0.6
      
                #     if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*0.9
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*0.9
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*0.9
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()*0.9

                #     if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()
            
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()
                   
      
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end)]
                #     df_ab1=df_ab1[(df_ab1.Prices>=start1) & (df_ab1.Prices<=end1)]
                #     df_ab2=df_ab2[(df_ab2.Prices>=start2) & (df_ab2.Prices<=end2)]
                #     df_ab3=df_ab3[(df_ab3.Prices>=start3) & (df_ab3.Prices<=end3)]
                #     return show_data4(      quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df1.shape[0],
                #                  total_response2=df1.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab1.Positive.mean(),
                #                  negative_reviews2=df_ab1.Negative.mean(),
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=df3.shape[0],
                #                  total_response4=df3.Response.sum(),
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df_ab3.Positive.mean(),
                #                  negative_reviews4=df_ab3.Negative.mean(),
                                 
                #                  )
                # if len(value_s)==5:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\{real[0]}\Datasets\detail_analysed.csv')
                #     df=pd.read_csv(f'E:\{real[0]}\Datasets\raw.csv')
                #     df_ab1=pd.read_csv(f'E:\{real[1]}\Datasets\detail_analysed.csv')
                #     df1=pd.read_csv(f'E:\{real[1]}\Datasets\raw.csv')
                #     df_ab2=pd.read_csv(f'E:\{real[2]}\Datasets\detail_analysed.csv')
                #     df2=pd.read_csv(f'E:\{real[2]}\Datasets\raw.csv')
                #     df_ab3=pd.read_csv(f'E:\{real[3]}\Datasets\detail_analysed.csv')
                #     df3=pd.read_csv(f'E:\{real[3]}\Datasets\raw.csv')
                #     df_ab4=pd.read_csv(f'E:\{real[4]}\Datasets\detail_analysed.csv')
                #     df4=pd.read_csv(f'E:\{real[4]}\Datasets\raw.csv')
                    
                    
                # if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()*pr[0]
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()*pr[0]
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()*pr[0]
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()*pr[0]
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()*pr[0]
                    
                # if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()*pr[0]
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()*pr[0]
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()*pr[0]
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()*pr[0]
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()*pr[0]
                # if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.6
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.max()*0.6
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.max()*0.6
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.max()*0.6
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.max()*0.6
                #     end4=df_ab4.Prices.max()
                # if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()*0.6
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()*0.6
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()*0.6
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()*0.6
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()*0.6
                # if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()*0.9
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()*0.9
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()*0.9
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()*0.9
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()*0.9
                # if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()
                # if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()


                    
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end)]
                #     df_ab1=df_ab1[(df_ab1.Prices>=start1) & (df_ab1.Prices<=end1)]
                #     df_ab2=df_ab2[(df_ab2.Prices>=start2) & (df_ab2.Prices<=end2)]
                #     df_ab3=df_ab3[(df_ab3.Prices>=start3) & (df_ab3.Prices<=end3)]
                #     df_ab4=df_ab4[(df_ab4.Prices>=start4) & (df_ab4.Prices<=end4)]
                #     return show_data5(  
                #                  quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=np.round((df_ab.Products.values[0]/df.shape[0])*df_ab.shape[0],0),
                #                  total_response1=df_ab.Response.values[0],
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df.Positive,
                #                  negative_reviews1=df.Negative,
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=np.round((df_ab1.Products.values[0]/df1.shape[0])*df_ab1.shape[0],0),
                #                  total_response2=df_ab1.Response.values[0],
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df.Positive,
                #                  negative_reviews2=df.Negative,
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=np.round((df_ab2.Products.values[0]/df2.shape[0])*df_ab2.shape[0],0),
                #                  total_response3=df_ab2.Response.values[0],
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df.Positive,
                #                  negative_reviews3=df.Negative,
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=np.round((df_ab3.Products.values[0]/df3.shape[0])*df_ab3.shape[0],0),
                #                  total_response4=df_ab3.Response.values[0],
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df.Positive,
                #                  negative_reviews4=df.Negative,
                                 
                                 
                #                  quality_x5=df_ab4.Base,
                #                  quality_y5=df_ab4.Rating,
                #                  avg_rating5=df_ab4.Rating.mean(),
                #                  avg_price5=df_ab4.Prices,
                #                  avgprice_x5=df_ab4.Prices,
                #                  avgprice_y5=df_ab4.Rating,
                #                  products_count5=np.round((df_ab4.Products.values[0]/df4.shape[0])*df_ab4.shape[0],0),
                #                  total_response5=df_ab4.Response.values[0],
                #                  labels5=real[4].replace('_',' '),
                #                  positive_reviews5=df.Positive,
                #                  negative_reviews5=df.Negative,
                                 
                #                  )
        else:
                value=''
                #Filtering Site Name
                if len(value_s)==1:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ae':
                            vali='Ali_Express'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset

                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')


                    if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*pr[0]
                    if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*pr[0]
                    if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.6
                        end=df_ab.Prices.max()
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*0.6
                    if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*0.9
                    if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:
                    
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()    

                    df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end) & (df_ab.cat.isin(tys))]
                    df=df[df.cat.isin(tys)]
                    return show_data(      
                                quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 )
                if len(value_s)==2:
                    lst=value_s
                    real=[]
                    for vali in lst:
                        if vali=='az':
                            vali='Amazon'
                            real.append(vali)
                        if vali=='ae':
                            vali='Ali_Express'
                            real.append(vali)
                        if vali=='ab':
                            vali='Ali_Baba'
                            real.append(vali)
                        if vali=='fp':
                            vali='Flikpart'
                            real.append(vali)
                        if vali=='dz':
                            vali='Daraz'
                            real.append(vali)
                    # Loading Dataset
                    df_ab=pd.read_csv(f'{real[0]}\\analysed.csv',encoding='latin')
                    df=pd.read_csv(f'{real[0]}\\raw.csv',encoding='latin')
                    df_ab1=pd.read_csv(f'{real[1]}\\analysed.csv',encoding='latin')
                    df1=pd.read_csv(f'{real[1]}\\raw.csv',encoding='latin')
                    
                    if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*pr[0]
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()*pr[0]
                        
                    
                    if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*pr[0]
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()*pr[0]
                       
                    if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.6
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.max()*0.6
                        end1=df_ab1.Prices.max()
                      
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()*0.6
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()*0.6
                     
                    if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()*0.9
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()*0.9
                       
                    if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                        start=df_ab.Prices.max()*0.3
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.max()*0.3
                        end1=df_ab1.Prices.max()
                       
                    if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                        start=df_ab.Prices.min()
                        end=df_ab.Prices.max()
                        start1=df_ab1.Prices.min()
                        end1=df_ab1.Prices.max()
                       
                  
                    df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end) & (df_ab.cat.isin(tys))]
                    df=df[df.cat.isin(tys)]
                    df_ab1=df_ab1[(df_ab1.Prices>=start) & (df_ab1.Prices<=end) & (df_ab1.cat.isin(tys))]
                    df1=df1[df1.cat.isin(tys)]
                    return show_data2(      
                                 quality_x1=df_ab.Base,
                                 quality_y1=df_ab.Rating,
                                 avg_rating1=df_ab.Rating.mean(),
                                 avg_price1=df_ab.Prices,
                                 avgprice_x1=df_ab.Prices,
                                 avgprice_y1=df_ab.Rating,
                                 products_count1=df.shape[0],
                                 total_response1=df.Response.sum(),
                                 labels1=real[0].replace('_',' '),
                                 positive_reviews1=df_ab.Positive.mean(),
                                 negative_reviews1=df_ab.Negative.mean(),
                                 
                                 
                                 quality_x2=df_ab1.Base,
                                 quality_y2=df_ab1.Rating,
                                 avg_rating2=df_ab1.Rating.mean(),
                                 avg_price2=df_ab1.Prices,
                                 avgprice_x2=df_ab1.Prices,
                                 avgprice_y2=df_ab1.Rating,
                                 products_count2=df1.shape[0],
                                 total_response2=df1.Response.sum(),
                                 labels2=real[1].replace('_',' '),
                                 positive_reviews2=df_ab1.Positive.mean(),
                                 negative_reviews2=df_ab1.Negative.mean(),
                                 
                                 
                                      
                                      )
                # if len(value_s)==3:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\\{real[0]}\\Datasets\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\\{real[0]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\raw.csv',encoding='latin')
      
        
                #     if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*pr[0]
                    
                    
                #     if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*pr[0]
               
                #     if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #         print('-----------------')
                #         start=df_ab.Prices.max()*0.6
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.6
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.6
                #         end2=df_ab2.Prices.max()
               
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*0.6
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*0.6
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*0.6
                      
                #     if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*0.9
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*0.9
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*0.9
              
                #     if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()
                   
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()
      

           
                    
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end) & (df_ab.cat.isin(tys))]
                #     df=df[df.cat.isin(tys)]
                    
                #     df_ab1=df_ab1[(df_ab1.Prices>=start) & (df_ab1.Prices<=end) & (df_ab1.cat.isin(tys))]
                #     df1=df1[df1.cat.isin(tys)]
                    
                #     df_ab2=df_ab2[(df_ab2.Prices>=start) & (df_ab2.Prices<=end) & (df_ab2.cat.isin(tys))]
                #     df2=df2[df2.cat.isin(tys)]
                #     return show_data3(      quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df1.shape[0],
                #                  total_response2=df1.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab1.Positive.mean(),
                #                  negative_reviews2=df_ab1.Negative.mean(),
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                                 
                #                  )
                # if len(value_s)==4:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\\{real[0]}\\Datasets\\analysed.csv',encoding='latin')
                #     df=pd.read_csv(f'E:\\{real[0]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\analysed.csv',encoding='latin')
                #     df1=pd.read_csv(f'E:\\{real[1]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\analysed.csv',encoding='latin')
                #     df2=pd.read_csv(f'E:\\{real[2]}\\Datasets\\raw.csv',encoding='latin')
                #     df_ab3=pd.read_csv(f'E:\\{real[3]}\\Datasets\\analysed.csv',encoding='latin')
                #     df3=pd.read_csv(f'E:\\{real[3]}\\Datasets\\raw.csv',encoding='latin')
                    
                    
                #     if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*pr[0]
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()*pr[0]
                 
                    
                #     if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*pr[0]
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*pr[0]
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*pr[0]
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()*pr[0]
          
                #     if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.6
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.6
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.6
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.max()*0.6
                #         end3=df_ab3.Prices.max()
              
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()*0.6
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()*0.6
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()*0.6
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()*0.6
      
                #     if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()*0.9
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()*0.9
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()*0.9
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()*0.9

                #     if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #         start=df_ab.Prices.max()*0.3
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.max()*0.3
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.max()*0.3
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.max()*0.3
                #         end3=df_ab3.Prices.max()
            
                #     if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #         start=df_ab.Prices.min()
                #         end=df_ab.Prices.max()
                #         start1=df_ab1.Prices.min()
                #         end1=df_ab1.Prices.max()
                #         start2=df_ab2.Prices.min()
                #         end2=df_ab2.Prices.max()
                #         start3=df_ab3.Prices.min()
                #         end3=df_ab3.Prices.max()
                   
      
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end) & (df_ab.cat.isin(tys))]
                #     df=df[df.cat.isin(tys)]
                #     df_ab1=df_ab1[(df_ab1.Prices>=start) & (df_ab1.Prices<=end) & (df_ab1.cat.isin(tys))]
                #     df1=df1[df1.cat.isin(tys)]
                #     df_ab2=df_ab2[(df_ab2.Prices>=start) & (df_ab2.Prices<=end) & (df_ab2.cat.isin(tys))]
                #     df2=df2[df2.cat.isin(tys)]
                #     df_ab3=df_ab3[(df_ab3.Prices>=start) & (df_ab3.Prices<=end) & (df_ab3.cat.isin(tys))]
                #     df3=df3[df3.cat.isin(tys)]
                #     return show_data4(      quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=df.shape[0],
                #                  total_response1=df.Response.sum(),
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df_ab.Positive.mean(),
                #                  negative_reviews1=df_ab.Negative.mean(),
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=df1.shape[0],
                #                  total_response2=df1.Response.sum(),
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df_ab1.Positive.mean(),
                #                  negative_reviews2=df_ab1.Negative.mean(),
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=df2.shape[0],
                #                  total_response3=df2.Response.sum(),
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df_ab2.Positive.mean(),
                #                  negative_reviews3=df_ab2.Negative.mean(),
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=df3.shape[0],
                #                  total_response4=df3.Response.sum(),
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df_ab3.Positive.mean(),
                #                  negative_reviews4=df_ab3.Negative.mean(),
                                 
                #                  )
                # if len(value_s)==5:
                #     lst=value_s
                #     real=[]
                #     for vali in lst:
                #         if vali=='az':
                #             vali='Amazon'
                #             real.append(vali)
                #         if vali=='ae':
                #             vali='Ali_Express'
                #             real.append(vali)
                #         if vali=='ab':
                #             vali='Ali_Baba'
                #             real.append(vali)
                #         if vali=='fp':
                #             vali='Flikpart'
                #             real.append(vali)
                #         if vali=='dz':
                #             vali='Daraz'
                #             real.append(vali)
                #     # Loading Dataset
                #     df_ab=pd.read_csv(f'E:\{real[0]}\Datasets\analysed.csv')
                #     df=pd.read_csv(f'E:\{real[0]}\Datasets\raw.csv')
                #     df_ab1=pd.read_csv(f'E:\{real[1]}\Datasets\analysed.csv')
                #     df1=pd.read_csv(f'E:\{real[1]}\Datasets\raw.csv')
                #     df_ab2=pd.read_csv(f'E:\{real[2]}\Datasets\analysed.csv')
                #     df2=pd.read_csv(f'E:\{real[2]}\Datasets\raw.csv')
                #     df_ab3=pd.read_csv(f'E:\{real[3]}\Datasets\analysed.csv')
                #     df3=pd.read_csv(f'E:\{real[3]}\Datasets\raw.csv')
                #     df_ab4=pd.read_csv(f'E:\{real[4]}\Datasets\analysed.csv')
                #     df4=pd.read_csv(f'E:\{real[4]}\Datasets\raw.csv')
                    
                    
                # if pr[0]==0.3 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()*pr[0]
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()*pr[0]
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()*pr[0]
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()*pr[0]
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()*pr[0]
                    
                # if pr[0]==0.6 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()*pr[0]
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()*pr[0]
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()*pr[0]
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()*pr[0]
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()*pr[0]
                # if pr[0]==0.9 and pr[1]=='Null' and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.6
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.max()*0.6
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.max()*0.6
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.max()*0.6
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.max()*0.6
                #     end4=df_ab4.Prices.max()
                # if pr[0]==0.3 and pr[1]==0.6 and pr[2]=="Null":
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()*0.6
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()*0.6
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()*0.6
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()*0.6
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()*0.6
                # if pr[0]==0.3 and pr[1]==0.9 and pr[2]=="Null":
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()*0.9
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()*0.9
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()*0.9
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()*0.9
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()*0.9
                # if pr[0]==0.6 and pr[1]==0.9 and pr[2]=='Null':
                #     start=df_ab.Prices.max()*0.3
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.max()*0.3
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.max()*0.3
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.max()*0.3
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.max()*0.3
                #     end4=df_ab4.Prices.max()
                # if pr[0]==0.3 and pr[1]==0.6 and pr[2]==0.9:              
                #     start=df_ab.Prices.min()
                #     end=df_ab.Prices.max()
                #     start1=df_ab1.Prices.min()
                #     end1=df_ab1.Prices.max()
                #     start2=df_ab2.Prices.min()
                #     end2=df_ab2.Prices.max()
                #     start3=df_ab3.Prices.min()
                #     end3=df_ab3.Prices.max()
                #     start4=df_ab4.Prices.min()
                #     end4=df_ab4.Prices.max()


                    
                #     df_ab=df_ab[(df_ab.Prices>=start) & (df_ab.Prices<=end) & (df_ab.cat.isin(tys))]
                #     df=df[df.cat.isin(tys)]
                #     df_ab1=df_ab1[(df_ab1.Prices>=start) & (df_ab1.Prices<=end) & (df_ab1.cat.isin(tys))]
                #     df1=df1[df1.cat.isin(tys)]
                #     df_ab2=df_ab2[(df_ab2.Prices>=start) & (df_ab2.Prices<=end) & (df_ab2.cat.isin(tys))]
                #     df2=df2[df2.cat.isin(tys)]
                #     df_ab3=df_ab3[(df_ab3.Prices>=start) & (df_ab3.Prices<=end) & (df_ab3.cat.isin(tys))]
                #     df3=df3[df3.cat.isin(tys)]
                #     df_ab4=df_ab4[(df_ab4.Prices>=start) & (df_ab4.Prices<=end) & (df_ab4.cat.isin(tys))]
                #     df4=df4[df4.cat.isin(tys)]
                #     return show_data5(  
                #                  quality_x1=df_ab.Base,
                #                  quality_y1=df_ab.Rating,
                #                  avg_rating1=df_ab.Rating.mean(),
                #                  avg_price1=df_ab.Prices,
                #                  avgprice_x1=df_ab.Prices,
                #                  avgprice_y1=df_ab.Rating,
                #                  products_count1=np.round((df_ab.Products.values[0]/df.shape[0])*df_ab.shape[0],0),
                #                  total_response1=df_ab.Response.values[0],
                #                  labels1=real[0].replace('_',' '),
                #                  positive_reviews1=df.Positive,
                #                  negative_reviews1=df.Negative,
                                 
                #                  quality_x2=df_ab1.Base,
                #                  quality_y2=df_ab1.Rating,
                #                  avg_rating2=df_ab1.Rating.mean(),
                #                  avg_price2=df_ab1.Prices,
                #                  avgprice_x2=df_ab1.Prices,
                #                  avgprice_y2=df_ab1.Rating,
                #                  products_count2=np.round((df_ab1.Products.values[0]/df1.shape[0])*df_ab1.shape[0],0),
                #                  total_response2=df_ab1.Response.values[0],
                #                  labels2=real[1].replace('_',' '),
                #                  positive_reviews2=df.Positive,
                #                  negative_reviews2=df.Negative,
                                 
                #                  quality_x3=df_ab2.Base,
                #                  quality_y3=df_ab2.Rating,
                #                  avg_rating3=df_ab2.Rating.mean(),
                #                  avg_price3=df_ab2.Prices,
                #                  avgprice_x3=df_ab2.Prices,
                #                  avgprice_y3=df_ab2.Rating,
                #                  products_count3=np.round((df_ab2.Products.values[0]/df2.shape[0])*df_ab2.shape[0],0),
                #                  total_response3=df_ab2.Response.values[0],
                #                  labels3=real[2].replace('_',' '),
                #                  positive_reviews3=df.Positive,
                #                  negative_reviews3=df.Negative,
                                 
                #                  quality_x4=df_ab3.Base,
                #                  quality_y4=df_ab3.Rating,
                #                  avg_rating4=df_ab3.Rating.mean(),
                #                  avg_price4=df_ab3.Prices,
                #                  avgprice_x4=df_ab3.Prices,
                #                  avgprice_y4=df_ab3.Rating,
                #                  products_count4=np.round((df_ab3.Products.values[0]/df3.shape[0])*df_ab3.shape[0],0),
                #                  total_response4=df_ab3.Response.values[0],
                #                  labels4=real[3].replace('_',' '),
                #                  positive_reviews4=df.Positive,
                #                  negative_reviews4=df.Negative,
                                 
                #                  quality_x5=df_ab4.Base,
                #                  quality_y5=df_ab4.Rating,
                #                  avg_rating5=df_ab4.Rating.mean(),
                #                  avg_price5=df_ab4.Prices,
                #                  avgprice_x5=df_ab4.Prices,
                #                  avgprice_y5=df_ab4.Rating,
                #                  products_count5=np.round((df_ab4.Products.values[0]/df4.shape[0])*df_ab4.shape[0],0),
                #                  total_response5=df_ab4.Response.values[0],
                #                  labels5=real[4].replace('_',' '),
                #                  positive_reviews5=df.Positive,
                #                  negative_reviews5=df.Negative,
                                 
                #                  )





############################################################################
#//////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////#
##################---Callback Function Starting Here----####################

@app.callback(
    Output("sidebar_collapse", "is_open"),
    [Input("_sidebar", "n_clicks")],
    [State("sidebar_collapse", "is_open")],
)
def sidebar_collapse(n, is_open):
   if n:       
       return not is_open
   else:
       return not is_open


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
   if n:
     return not is_open
   return  is_open
 

@app.callback(
    Output('filter_collapse','is_open'),
    [Input('filter_','n_clicks')],
    [State('filter_collapse','is_open')]
    )
def filter_runner(n,is_open):
    if n:
        return not is_open
    return is_open



value=''
_about=False
_filter=False
_chart=False
@app.callback(Output('output','children'),
              
               [Input('ddn','value'),
                Input('realid','value'),
                Input('prices','value'),
                Input('items1','value'),
                Input('items2','value'),
                Input('items3','value'),            
               ]
              
              )
#Main Functions for Showing Output and Controling the Whole Project
def genrator(value_s,side,prcs,tys,hdsfree,shoes):
    print('-----------',prcs,'---------------')
    print('-------------',tys,'--------------')
    print('------------',shoes,'-------------')
    temp=[]
    text=''
    if side==1: 
        print(side)
        if prcs==None:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
                temp=sorted(temp)
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=['Null','Null','Null'])     
        if prcs==['low']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.3,'Null','Null'])     
        if prcs==['normal']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.6,'Null','Null'])     
        if prcs==['high']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.9,'Null','Null'])     
        if prcs==['low','normal'] or prcs==['normal','low']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.3,0.6,'Null'])     
        if prcs==['low','high'] or prcs==['high','low']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.3,0.9,'Null'])     
        if prcs==['normal','high'] or prcs==['high','normal']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.6,0.9,'Null'])     
        if prcs==['low','normal','high'] or prcs==['normal','high','low'] or prcs==['high','low','normal'] or prcs==['normal','low','high'] or prcs==['high','normal','low'] or prcs==['low','high','normal']:
            if tys!=None:
                for s in tys:
                    temp.append(s)
            if shoes!=None:
                for x in shoes:
                    temp.append(x)
            if hdsfree!=None:
                for y in hdsfree:
                    temp.append(y)
            for val in sorted(temp):
                text+=val
            print('\\\\\\\\\\\\\\\\\\',text)
            #Defining at 2295
            return conditions(value_s,temp,pr=[0.3,0.6,0.9])     
     
                
        
    if side==2:   
        print(side)
        about_data=html.Div([
            
            html.H5(f'i am M Ameer Hamza (Hamza Ansari) i develop this app for helping to buy best thing '
                       ,style={'color':'white','margin-top':'200px'
                               ,'margin-left':'100px'}),
            html.Br(),html.Br(),html.Br(),html.Br(), html.Br(),html.Br(),html.Br(),html.Br(), html.Br(),html.Br(),html.Br(),html.Br(),
            html.Div([
                          
                            
                            
                             html.Div([ 
                                html.A( 'Stay_Connected',style={'color':'white','margin-top':'15px'
                               ,'margin-left':'100px'}),
                                
                                html.A(
                                       [html.I(className="fa fa-github")]
                                ,href='https://github.com/hamzaansarics',style={'margin-left':'100px'}),
                                html.A(
                                       [html.I(className="fa fa-linkedin")]
                                ,href='https://www.linkedin.com/in/hamzaansarics',style={'margin-left':'20px'}),
                                                         html.A(
                                       [html.I(className="fa fa-twitter")]
                                ,href='https://twitter.com/mehamzaansari',style={'margin-left':'20px'}),html.A(
                                       [html.I(className="fa fa-facebook")]
                                ,href='https://web.facebook.com/mehamzaansari',style={'margin-left':'20px'}),
                            ],className='d-flex')
                      
                        
                        
                        
          ],className='col-xl-3 col-lg-4')
            
            ])
        return about_data
    

   
        
if __name__=='__main__':
    app.run_server(debug=False)