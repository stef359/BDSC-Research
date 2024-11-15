import pandas as pd
import matplotlib.pyplot as plt

# Data
liquor_data = pd.read_csv(('Data/Liquor_Outlets_Density.csv'))
violent_crime_data = pd.read_csv('Data/Violent_Crime.csv')
property_crime_data = pd.read_csv('Data/Property_Crime.csv')
all_crime_data = pd.read_csv('Data/All_Crime.csv')

# Merge (CSA2010)
merged_violent = pd.merge(liquor_data, violent_crime_data, on='CSA2010')
merged_property = pd.merge(liquor_data, property_crime_data, on='CSA2010')
merged_all = pd.merge(liquor_data, all_crime_data, on='CSA2010')

# Crime rate
avg_violent_crime = merged_violent['viol21'].mean()
avg_property_crime = merged_property['prop21'].mean()
avg_all_crime = merged_all['crime21'].mean()

# Bar Chart
crime_types = ['Violent Crime', 'Property Crime', 'All Crime']
crime_rates = [avg_violent_crime, avg_property_crime, avg_all_crime]

# Plots
plt.figure(figsize=(10, 6))
plt.bar(crime_types, crime_rates, color=['blue', 'orange', 'green'])
plt.title('Average Crime Rates Near Liquor Outlets by Crime Type (2021)', fontsize=18)
plt.xlabel('Crime Type', fontsize=14)
plt.ylabel('Average Crime Rate (Per 1,000)', fontsize=14)
plt.show()