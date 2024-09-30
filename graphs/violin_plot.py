import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_violin_plot():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: The 'Category' and 'Value' columns are required in the CSV file.")
            return

        # Set the seaborn style
        sns.set(style='whitegrid')

        # Create the violin plot
        sns.violinplot(x='Category', y='Value', data=data)
        plt.title('Violin Plot')

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_violin_plot()
