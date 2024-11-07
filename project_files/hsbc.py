# hsbc.py
import dash
from dash import html
from data import fetch_latest_close_price

latest_date, latest_close_price = fetch_latest_close_price("HSBC")

# Format and display the output
if latest_close_price is not None:
    print(f"Date: {latest_date}, Close Price: ${latest_close_price:.2f}")
else:
    print("No data available for the specified date range.")



def create_hsbc_tab():
    return html.Div([
        # Container for the two main sections
        html.Div([
            # Left section with Close Price Prediction and new cards
            html.Div([
                # First card (Close Price Prediction)
                html.Div([
                    html.H3("Close Price Prediction", style={
                        'font-size': '14px',
                        'color': '#ffffff',
                        'margin': '0',            # Remove default H3 margin
                        'textAlign': 'center',
                    }),
                ], 
                style={
                    'backgroundColor': '#001f3f', # Navy blue background
                    'border-radius': '5px',
                    'width': '100%',              # Full width for the title card
                    'height': '40px',             # Adjust height as needed
                    'display': 'flex',            # Flex display for centering
                    'align-items': 'center',      # Center content vertically
                    'justify-content': 'center',  # Center content horizontally
                    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.1)',
                }),
                # Container for the two new cards (Previous Day Close and Current Date Prediction)
                html.Div([
                    # New card for Previous Day Close
                    html.Div([
                        html.H3("Previous Day Close", style={
                            'font-size': '16px',
                            'color': '#000000',  # Black text
                            'margin': '0',
                            'textAlign': 'center',
                        }),
                        html.P(f"Date: {latest_date}" if latest_date is not None else "Date: N/A",
                        style={
                            'font-size': '12px',
                            'color': '#000000',  # Black text
                            'margin': '5px 0',
                            'textAlign': 'center',
                        }),
                        html.P(
                        f"Close Price: ${latest_close_price:.2f}" if latest_close_price is not None else "Close Price: N/A",    
                        style={    
                            'font-size': '16px',
                            'color': '#000000',  # Black text
                            'margin': '5px 0',
                            'textAlign': 'center',
                        }),
                    ], 
                    style={
                        'backgroundColor': '#ffffff', # White background
                        'border-radius': '5px',
                        'width': '50%',              # Each card takes up half of the row
                        'padding': '10px',           # Padding inside the card
                        'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.1)',
                        'margin-top': '10px',         # Space above this card
                    }),
                    # New card for Current Date Prediction
                    html.Div([
                        html.H3("Current Date Prediction", style={
                            'font-size': '16px',
                            'color': '#000000',  # Black text
                            'margin': '0',
                            'textAlign': 'center',
                        }),
                        html.P("Current Date: YYYY-MM-DD", style={
                            'font-size': '12px',
                            'color': '#000000',  # Black text
                            'margin': '5px 0',
                            'textAlign': 'center',
                        }),
                        html.P("Prediction: Higher", style={
                            'font-size': '16px',
                            'color': '#000000',  # Black text
                            'margin': '5px 0',
                            'textAlign': 'center',
                        }),
                    ], 
                    style={
                        'backgroundColor': '#ffffff', # White background
                        'border-radius': '5px',
                        'width': '50%',              # Each card takes up half of the row
                        'padding': '10px',           # Padding inside the card
                        'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.1)',
                        'margin-top': '10px',         # Space above this card
                    }),
                ], style={
                    'display': 'flex',             # Use flexbox to lay out the cards
                    'flex-direction': 'row',       # Stack cards horizontally
                    'gap': '10px',                 # Space between the cards
                    'margin-top': '10px'           # Space above the row of cards
                }),
            ], style={
                'width': '50%',                # Set width for left section
                'display': 'flex',
                'flex-direction': 'column',    # Stack title card and card row vertically
                'gap': '10px',                 # Space between title card and card row
            }),
            # Right section (Business Summary)
            html.Div([
                # Business Summary title card
                html.Div([
                    html.H3("Business Summary", style={
                        'font-size': '14px',
                        'color': '#ffffff',
                        'margin': '0',
                        'textAlign': 'center',
                    }),
                ], 
                style={
                    'backgroundColor': '#001f3f', # Navy blue background
                    'border-radius': '5px',
                    'width': '100%',              # Full width within the right column
                    'height': '40px',            
                    'display': 'flex',           
                    'align-items': 'center',      
                    'justify-content': 'center',  
                    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.1)',
                }),
                # Additional card below Business Summary title card with description
                html.Div([
                    html.P("HSBC Holdings plc provides banking and financial services. It operates in three segments:", style={
                        'font-size': '14px',      
                        'color': '#333333',       
                        'margin': '10px',         
                        'textAlign': 'left',
                    }),
                    html.Ul([
                        html.Li([
                            html.B("Wealth and Personal Banking:"),  " Offers personal banking, wealth management, and investment products like savings accounts, loans, credit cards, insurance, and asset management for individuals and high net worth clients."
                        ]),
                        html.Li([
                            html.B("Commercial Banking:"), " Provides loans, treasury, cash management, insurance, trade finance, and advisory services for SMEs, mid-market firms, and corporates."
                        ]),
                        html.Li([
                            html.B("Global Banking and Markets:"), " Delivers financing, advisory, and trading services across credit, rates, foreign exchange, equities, and securities, catering to government, corporate, and institutional clients."
                        ])
                    ], 
                    style={
                        'font-size': '14px',
                        'padding-left': '10px',  # Indent bullet points
                    }),
                ], 
                style={
                    'backgroundColor': '#f9f9f9', # Light background for contrast
                    'border-radius': '5px',
                    'width': '100%',             # Match the width of the title card
                    'padding': '5px',           # Padding inside the description card
                    'box-shadow': '2px 2px 8px rgba(0, 0, 0, 0.1)',
                    'margin-top': '10px'         # Space between the title and description card
                }),
            ], style={'width': '50%'}),  # Set width for right section
        ], 
        style={
            'display': 'flex',              # Use flexbox for layout
            'gap': '10px',                 # Space between left and right sections
            'margin-top': '20px'
        })
    ])
