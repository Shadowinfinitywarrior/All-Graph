import pandas as pd
import matplotlib.pyplot as plt

def create_bubble_chart():
    try:
        # Read the CSV file
        data = pd.read_csv('data/sample_data.csv')

        # Check if 'Category' and 'Value' columns exist
        if 'Category' not in data.columns or 'Value' not in data.columns:
            print("Error: 'Category' and 'Value' columns must be present in the CSV.")
            return

        # Convert Category to numerical values for plotting
        category_codes = pd.Categorical(data['Category']).codes

        # Create the bubble chart
        plt.scatter(category_codes, data['Value'], s=data['Value'] * 10, alpha=0.5)

        # Customize the plot
        plt.title('Bubble Chart')
        plt.xlabel('Category')
        plt.ylabel('Value')

        # Adjust x-ticks to show category names
        plt.xticks(ticks=range(len(data['Category'])), labels=data['Category'])

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'data/sample_data.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not formatted correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_bubble_chart()
