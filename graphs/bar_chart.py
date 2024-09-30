import pandas as pd
import matplotlib.pyplot as plt

def create_bar_chart():
    try:
        # Read CSV file, skipping bad lines
        data = pd.read_csv('data/sample_data.csv', delimiter=',', on_bad_lines='skip')

        # Check if required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: 'Category' and 'Value' columns must be present in the CSV.")
            return

        # Create bar chart
        plt.bar(data['Category'], data['Value'], color='blue')
        plt.title('Bar Chart')
        plt.xlabel('Category')
        plt.ylabel('Value')
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_bar_chart()
