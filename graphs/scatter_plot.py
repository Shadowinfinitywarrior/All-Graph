import pandas as pd
import matplotlib.pyplot as plt

def create_scatter_plot():
    try:
        # Load the data
        data = pd.read_csv('data/sample_data.csv')

        # Check if the required columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: The 'Category' and 'Value' columns are required in the CSV file.")
            return

        # Convert categories to numeric if they are not already
        if data['Category'].dtype == 'object':
            data['Category'] = pd.Categorical(data['Category']).codes

        # Create the scatter plot
        plt.scatter(data['Category'], data['Value'])
        plt.title('Scatter Plot')
        plt.xlabel('Category')
        plt.ylabel('Value')

        # Optional: Set x-ticks to show original category labels
        plt.xticks(ticks=range(len(data['Category'].unique())), labels=data['Category'].unique(), rotation=45)

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_scatter_plot()
