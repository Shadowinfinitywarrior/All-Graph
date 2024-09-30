import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: The 'Category' and 'Value' columns are required in the CSV file.")
            return

        # Filter out zero values if any
        data = data[data['Value'] > 0]

        # Create the pie chart
        plt.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart')

        # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.axis('equal')

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_pie_chart()
