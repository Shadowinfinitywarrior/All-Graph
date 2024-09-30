import matplotlib.pyplot as plt
import numpy as np

def create_waterfall_chart():
    # Data for the waterfall chart
    labels = ['Start', 'Gain', 'Loss', 'End']
    values = [100, 50, -30, 0]  # Setting the last value to 0 for cumulative calculation

    # Calculate cumulative values
    cumulative_values = np.zeros(len(values) + 1)
    cumulative_values[0] = values[0]  # Starting value
    for i in range(1, len(values) + 1):
        cumulative_values[i] = cumulative_values[i - 1] + values[i - 1]

    # Create bars for the waterfall chart
    colors = ['blue' if val >= 0 else 'red' for val in values]  # Blue for gain, red for loss
    plt.bar(labels, cumulative_values[1:], color=colors, alpha=0.7)
    
    # Adding lines to represent the transitions
    for i in range(len(labels) - 1):
        plt.plot([labels[i], labels[i + 1]], [cumulative_values[i], cumulative_values[i + 1]], color='black')

    # Set titles and labels
    plt.title('Waterfall Chart')
    plt.ylabel('Value')
    
    # Show the plot
    plt.show()

# Run the function
create_waterfall_chart()
