import yfinance as yf

# Function to fetch the latest close price and date for a specific stock (e.g., HSBC)
def fetch_latest_close_price(ticker):
    # Download the data for the given stock ticker
    data = yf.download(ticker, start='2020-01-01', end='2024-11-04')
    
    # Check if data is not empty to avoid errors
    if not data.empty:
        # Get the latest close price and the corresponding date
        latest_date = data.index[-1].strftime('%Y-%m-%d')  # Format date as 'YYYY-MM-DD'
        latest_close_price = data['Close'].iloc[-1].item()  # Get the latest close price as a scalar
        return latest_date, latest_close_price
    else:
        return None, None  # Return None if there's no data
