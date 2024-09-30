import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_radar_chart():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: The 'Category' and 'Value' columns are required in the CSV file.")
            return

        # Ensure there are enough categories
        if len(data) < 2:
            print("Error: At least two categories are required to create a radar chart.")
            return

        categories = list(data['Category'])
        values = list(data['Value'])

        # Ensure values are numeric
        values = [float(value) for value in values]

        N = len(categories)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

        # Close the loop
        values += values[:1]
        angles += angles[:1]

        # Create the radar chart
        plt.subplot(111, polar=True)
        plt.fill(angles, values, color='red', alpha=0.25)
        plt.plot(angles, values, color='red', linewidth=2)
        plt.xticks(angles[:-1], categories)
        plt.title('Radar Chart')

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_radar_chart()
