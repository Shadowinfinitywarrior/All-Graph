import matplotlib.pyplot as plt

def create_funnel_chart():
    # Funnel stages and corresponding values
    stages = ['Awareness', 'Interest', 'Desire', 'Action']
    values = [1000, 600, 300, 150]

    # Reverse the stages and values to represent a funnel shape
    stages.reverse()
    values.reverse()

    # Create the funnel chart (horizontal bar chart)
    plt.barh(stages, values, color='skyblue', edgecolor='black')

    # Customize the plot
    plt.title('Funnel Chart')
    plt.xlabel('Number of Users')
    
    # Remove the top and right spines to make it look cleaner
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    # Show the chart
    plt.show()

# Run the function
create_funnel_chart()
