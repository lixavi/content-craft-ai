# utils/data_visualization.py

import matplotlib.pyplot as plt

def visualize_data_distribution(data):
    # Visualize the distribution of data
    plt.hist(data, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Data Distribution')
    plt.grid(True)
    plt.show()
