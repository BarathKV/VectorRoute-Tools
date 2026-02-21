import yfinance as yf

def get_stock_price(symbol: str):
    """
    Get the latest stock price for a symbol using Yahoo Finance API.
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    
    Returns:
        Float representing the current closing price of the stock
        
    Raises:
        Exception: If API request fails or stock symbol not found
    """
    symbol = symbol.upper().strip()
    
    try:
        # Download the stock data
        stock = yf.Ticker(symbol)
        
        # Get the historical data (last 1 day to get latest price)
        hist = stock.history(period="1d")
        
        if hist.empty:
            raise ValueError(f"Stock symbol '{symbol}' not found or no data available")
        
        # Get the latest closing price
        close_price = hist['Close'].iloc[-1]
        
        if close_price is None or close_price == 0:
            raise ValueError(f"Could not retrieve closing price for {symbol}")
        
        return float(close_price)
    except ValueError:
        raise
    except Exception as e:
        raise Exception(f"Failed to fetch stock price for {symbol}: {str(e)}")

