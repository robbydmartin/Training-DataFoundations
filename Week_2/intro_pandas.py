# pandas is a python library used for data manipulation and analysis
#   it provides data structures like Dataframes and Series to work with structured data
#   it also offers funcitonalities for data cleaning, transformation, aggregation, and visualization

import pandas as pd
import matplotlib.pyplot as plt

# Create a simple data frame
data = {
    'Name': ['Alice', 'David', 'Charlie', 'Bob'],
    'Age': [24, 42, 19, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a data frame using the above dicitonary
df = pd.DataFrame(data)
print(df)

# Access rows by index location
#   uses the .iloc[x] (index location where x is the desired index)
print('\nFirst Row:\n', df.iloc[0])

# Access columns
#   just use the column name
print('\nNames Column\n', df['Name'])

# Filter data using a condition
older_than_30 = df[df['Age'] >= 30]
print('\nAdults 30+:\n', older_than_30)

# Add a new column
df['Occupation'] = ['Doctor', 'Biologist', 'Chef', 'Engineer']
print('\nNew Occupation column:\n', df)

# Simple stats
print('\nAverage Age:\n', df['Age'].mean())
print('\nMaximum Age:\n', df['Age'].max())
print('\nSummary Statistics:\n', df.describe()) # this will show multiple stats on our data

# Sort data
sorted_df = df.sort_values(by='Age')
print('\nSorted by Age:\n', sorted_df)

##################################################################

# Now Accessing data from CSV
vehicle_df = pd.read_csv('./Week_2/data/Electric_Vehicle_Population_Data.csv')
# print('\nVehicle DataFrame:\n', vehicle_df.head())
print('\nVehicle DataFrame:\n', vehicle_df.info()) # will give summary of our data frame

# Basic selection and filtering
# select each unique vehicle make: 
vehicle_makes = vehicle_df['Make'].unique() # choose the column name
print('\nUnique Makes:\n', vehicle_makes) # will tell the data type as well

# Filter vehicle made by Tesla
tesla_vehicles = vehicle_df[vehicle_df['Make'] == 'TESLA']
print('\nTesla Vehicles:\n', tesla_vehicles)

# Filter using NOT using the ~ operator in pandas (can't use not keyword or !)
non_tesla_vehicles = vehicle_df[~(vehicle_df['Make'] == 'TESLA')]
print('\nNon-Tesla Vehicles:\n', non_tesla_vehicles.head(6))

# We can aggregate some data
# Lets get the average electric range by vehicle make
#   and filter out zero vaules
# avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean() # filtering out zero vaules, group by Make and getting the mean
avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean()
print('\nAverage Electric Range by Make:\n', avg_range_by_make)

# Can do multiple aggregation with different columns
double_aggro = vehicle_df.groupby(['Make']).agg(
    avg_range=('Electric Range', 'mean'),
    leg_dis=('Legislative District', 'sum')
)
print(double_aggro)

# Finally we can visualize our data using matplotlib
# We can create a Figure - a matplotlib object that reprents the entire figure/plot area
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot the average electric range by vehicle as a bar chart
avg_range_by_make.plot(kind='bar', ax=axes[0,0], title='Average Electric Range by Vehicle Make')
plt.xlabel("Vehicle Make")
plt.ylabel("Average Electric Range(miles)")

# Plot the count of non-tesla vehicle by model year
non_tesla_vehicles['Model Year'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], title='Count of Non-Teslas by Model Year', xlabel='Model Year', ylabel='Number of Vehicles')

plt.show()

# Finally, we can export our modified DataFrame to a new CSV file
non_tesla_vehicles.to_csv('./Week_2/data/modified_vehicle_data.csv', index=False)
