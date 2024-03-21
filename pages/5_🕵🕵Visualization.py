import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have your data in a pandas dataframe called 'df'
chart_type = "bar"  # Change "bar" to "pie" or "line" for other charts

# Create the bar chart
if chart_type == "bar":
  plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
  plt.bar(df["workclass"].value_counts().index, df["workclass"].value_counts().values)
  plt.xlabel("Work Class")
  plt.ylabel("Count")
  plt.title("Age Distribution by Work Class")
  plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
  plt.tight_layout()
  plt.show()

# Add similar logic for "pie" and "line" charts using plt.pie and sns.lineplot respectively
