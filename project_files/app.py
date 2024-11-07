import dash
from dash import dcc, html
from dash.dependencies import Input, Output
# Import tab content from separate files
from welcome import create_welcome_tab
from hsbc import create_hsbc_tab
#from barclays import create_barclays_tab
#from lloyds import create_lloyds_tab
#from natwest import create_natwest_tab
#from standardchartered import create_stanchart_tab

# Create a Dash application
app = dash.Dash(__name__)

app.layout = html.Div([
    # Title with darker blue background and white text
    html.Div(
        children="FTSE 100 Listed Banks Close Price Predictions Dashboard",
        style={
            'backgroundColor': '#001f3f',  # Darker blue background
            'color': 'white',              # White text color
            'padding': '20px',             # Padding around the text
            'textAlign': 'center',         # Center align the text
            'fontSize': '18px',            # Increase font size
            'fontWeight': 'bold',          # Bold text
        }
    ),
    
    # Tabs section
    dcc.Tabs(id='tabs', value='welcome', children=[
        dcc.Tab(label='Welcome', value='welcome'),
        dcc.Tab(label='HSBC', value='hsbc'),
        dcc.Tab(label='Barclays', value='barclays'),
        dcc.Tab(label='Lloyds', value='lloyds'),
        dcc.Tab(label='Natwest', value='natwest'),
        dcc.Tab(label='Standard Chartered', value='stanchart'),
    ]),
    # Content area for the selected tab
    html.Div(id='tabs-content')
])
# Callback to update the content of each tab
@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'welcome':
        return create_welcome_tab()  # Content for Welcome tab
    elif tab == 'hsbc':
        return create_hsbc_tab()     # Content for HSBC tab
    elif tab == 'barclays':
        return create_barclays_tab() # Content for Barclays tab
    elif tab == 'lloyds':
        return create_lloyds_tab()   # Content for Lloyds tab
    elif tab == 'natwest':
        return create_natwest_tab()  # Content for Natwest tab
    elif tab == 'stanchart':
        return create_stanchart_tab()  # Content for Standard Chartered tab
    # Add additional cases if you add more tabs in the future
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
