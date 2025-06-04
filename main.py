import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')  # Replace 'data.csv' with your actual dataset file

# Perform basic analysis
print("Data Head:")
print(data.head())  # Display first few rows of the dataset
print("\nSummary Statistics:")
print(data.describe())  # Display summary statistics

# Plot a simple histogram for a specific column
data['column_name'].plot(kind='hist')  # Replace 'column_name' with a real column name from your dataset
plt.title("Histogram of Column")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
