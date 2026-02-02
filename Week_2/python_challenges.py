import matplotlib.pyplot as plt
import pandas as pd

'''
Python Review Challenges

Challenge 1
'''
#A weather station recorded the average temperature over 7 days.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [12, 14, 15, 13, 16, 18, 17]

#Challenge Tasks

#Create a line plot showing temperature changes over the week.

'''Add:

A meaningful title

X-axis label

Y-axis label

Use circle markers and a dashed line.

Highlight the warmest day with a different color.

Add a grid.

(Bonus) Annotate the warmest temperature value on the chart.
'''

warmest_day_temp = max(temperatures)
temp_index = temperatures.index(warmest_day_temp)
warmest_day = days[temp_index]

plt.figure(figsize=(8, 6))
plt.plot(days, temperatures, marker='o', linestyle='dashed', color='b')
plt.scatter(warmest_day, warmest_day_temp, color='r', s=100)
plt.annotate(warmest_day_temp, (warmest_day, warmest_day_temp), xytext=(warmest_day, warmest_day_temp),textcoords='offset pixels')
plt.title("Average Daily Temperature")
plt.xlabel("Day of the Week")
plt.ylabel("Average Temperature (C)")
plt.grid(True)
plt.show()


# Challenge 2


#A small shop tracked its monthly sales for the first half of the year.
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1350, 1100, 1500, 1600, 1550]
}

df = pd.DataFrame(data)

'''
Challenge Tasks

Use pandas to inspect the data.

Create a line plot of sales over the months using matplotlib.

Add:

A title

X-axis label

Y-axis label

Highlight the month with the highest sales.

Add a grid.

(Bonus) Display the exact sales value for the highest month on the chart.
'''
# Inspect the data
print("Dataframe information\n", df)
print("Statisical information\n", df.describe())
average_monthly_sales = df['Sales'].mean()
print("\nAverage monthly sales: $", average_monthly_sales)

max_sales = df['Sales'].max()
max_value_index = df['Sales'].idxmax()
max_sales_month = df.at[max_value_index, 'Month']
print("Max sales: $", max_sales)
print("Max sales month:", max_sales_month)

plt.plot(df['Month'], df['Sales'], marker='o', linestyle='dashed', color='b')
plt.scatter(max_sales_month, max_sales, color='r', s=100)
plt.annotate(max_sales_month, (max_sales_month, max_sales), xytext=(max_sales_month, max_sales), textcoords='offset pixels')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total sales')
plt.grid(True)
plt.show()