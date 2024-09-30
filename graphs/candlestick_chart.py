import pandas as pd
import mplfinance as mpf

def create_candlestick_chart():
    try:
        # Read the CSV file and parse the 'Date' column
        data = pd.read_csv('data/candlestick_data.csv', parse_dates=['Date'], index_col='Date')

        # Check if required columns exist
        required_columns = ['Open', 'High', 'Low', 'Close']
        if not all(col in data.columns for col in required_columns):
            print(f"Error: The CSV file must contain the following columns: {required_columns}")
            return

        # Create the candlestick chart
        mpf.plot(data, type='candle', style='charles', title='Candlestick Chart', volume=False)

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_candlestick_chart()
