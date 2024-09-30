import tkinter as tk
import subprocess
from tkinter import messagebox

def run_program(graph_type):
    try:
        if graph_type == 'Bar Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/bar_chart.py'])
        elif graph_type == 'Line Graph':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/line_graph.py'])
        elif graph_type == 'Pie Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/pie_chart.py'])
        elif graph_type == 'Histogram':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/histogram.py'])
        elif graph_type == 'Scatter Plot':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/scatter_plot.py'])
        elif graph_type == 'Box Plot':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/box_plot.py'])
        elif graph_type == 'Area Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/area_chart.py'])
        elif graph_type == 'Heatmap':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/heatmap.py'])
        elif graph_type == 'Bubble Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/bubble_chart.py'])
        elif graph_type == 'Radar Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/radar_chart.py'])
        elif graph_type == 'Funnel Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/funnel_chart.py'])
        elif graph_type == 'Waterfall Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/waterfall_chart.py'])
        elif graph_type == 'Violin Plot':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/violin_plot.py'])
        elif graph_type == 'Candlestick Chart':
            subprocess.Popen(['python', 'C:/Users/User/Downloads/data_visualization_project/graphs/candlestick_chart.py'])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_gui():
    root = tk.Tk()
    root.title("Data Visualization Project")

    label = tk.Label(root, text="Click a button to display a graph:", font=("Arial", 14))
    label.pack(pady=10)

    graph_types = [
        'Bar Chart',
        'Line Graph',
        'Pie Chart',
        'Histogram',
        'Scatter Plot',
        'Box Plot',
        'Area Chart',
        'Heatmap',
        'Bubble Chart',
        'Radar Chart',
        'Funnel Chart',
        'Waterfall Chart',
        'Violin Plot',
        'Candlestick Chart'
    ]

    for graph_type in graph_types:
        button = tk.Button(root, text=graph_type, command=lambda g=graph_type: run_program(g), width=25)
        button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, width=25)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
