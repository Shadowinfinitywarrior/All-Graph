import pandas as pd
import matplotlib.pyplot as plt

def create_line_graph():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: The 'Category' and 'Value' columns are required in the CSV file.")
            return

        # Create the line graph
        plt.plot(data['Category'], data['Value'], marker='o', color='orange')

        # Customize the plot
        plt.title('Line Graph')
        plt.xlabel('Category')
        plt.ylabel('Value')
        plt.grid()

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_line_graph()
