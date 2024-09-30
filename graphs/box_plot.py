import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_box_plot():
    try:
        # Read the CSV file
        data = pd.read_csv('data/sample_data.csv')

        # Check if required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: 'Category' and 'Value' columns must be present in the CSV.")
            return

        # Create the box plot
        sns.boxplot(x=data['Category'], y=data['Value'])

        # Add a title and labels
        plt.title('Box Plot')
        plt.xlabel('Category')
        plt.ylabel('Value')

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_box_plot()
