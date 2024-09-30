import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap():
    try:
        # Load the data
        data = pd.read_csv('data/heatmap_data.csv')

        # Check if required columns exist
        required_columns = ['Category', 'Subcategory', 'Value']
        if not all(col in data.columns for col in required_columns):
            print(f"Error: The CSV file must contain the following columns: {required_columns}")
            return

        # Pivot the data to create a matrix for the heatmap
        data_matrix = data.pivot(index="Category", columns="Subcategory", values="Value")

        # Create the heatmap
        sns.heatmap(data_matrix, annot=True, cmap="coolwarm", fmt=".1f")

        # Customize the plot
        plt.title('Heatmap')
        plt.xlabel('Subcategory')
        plt.ylabel('Category')
        
        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_heatmap()
