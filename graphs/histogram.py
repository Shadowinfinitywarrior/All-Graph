import pandas as pd
import matplotlib.pyplot as plt

def create_histogram():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the 'Value' column exists
        if 'Value' not in data.columns:
            print("Error: The 'Value' column is missing from the CSV file.")
            return

        # Create the histogram
        plt.hist(data['Value'], bins=5, color='skyblue', edgecolor='black')
        
        # Customize the plot
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_histogram()
