'''
You are building a simple fitness tracking analysis tool.
A CSV file contains daily step counts for a user.
Your program will:

Read data from a file

Let the user choose how many days to analyze

Use NumPy for calculations

Use pandas for data handling

Use matplotlib for visualization

Your Task:
Load the CSV file using pandas.

Ask the user:

"How many days of data would you like to analyze (1–7)?"

Use the user’s input to select the first N days from the dataset.

Use NumPy to calculate:
Average steps
Maximum steps
Minimum steps

Display the results in the terminal.

Plot a bar chart of steps for the selected days.

Add:
Title
Axis labels
Grid

Highlight the day with the highest steps in a different color.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('./Week_2/data/steps.csv')

# Get user input
while True:
    user_input = input('How many days of data would you like to analyze (1-7)? ')
    try:
        # Try to convert input to an integer
        choice = int(user_input)
        # Check if integer is a valid choice
        if choice < 1 or choice > 7:
            print("Please enter a number between 1 and 7")
        else:
            break
    # Raise exception if the input is not an integer
    except ValueError:
        print("Please enter a number between 1 and 7")

# average_steps = df[:choice]['Steps'].mean()
# max_steps = df[:choice]['Steps'].max()
# min_steps = df[:choice]['Steps'].min()

average_steps = df['Steps'].iloc[:choice].mean()
max_steps = df['Steps'].iloc[:choice].max()
min_steps = df['Steps'].iloc[:choice].min()

print(f"Average steps: {average_steps}")
print(f'Maximum steps: {max_steps}')
print(f'Minimum steps: {min_steps}')

# Create list of colors for highlighting the max value
colors = ['red' if step == max_steps else 'blue' for step in df['Steps'].iloc[:choice] ]

plt.bar(df['Day'].iloc[:choice], df['Steps'].iloc[:choice], color=colors)
plt.title(f"Steps per day for first {choice} days of the week")
plt.xlabel("Day of the week")
plt.ylabel("Number of steps")
plt.grid(True)
plt.show()
