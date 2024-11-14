import pandas as pd
import matplotlib.pyplot as plt

# Data
university_data = pd.read_csv('Data/Universities_and_Colleges.csv')
violent_crime_data = pd.read_csv('Data/Violent_Crime.csv')
property_crime_data = pd.read_csv('Data/Property_Crime.csv')
all_crime_data = pd.read_csv('Data/All_Crime.csv')

# Merge (CSA2010)
merged_violent = pd.merge(university_data, violent_crime_data, on='CSA2010')
merged_property = pd.merge(university_data, property_crime_data, on='CSA2010')
merged_all = pd.merge(university_data, all_crime_data, on='CSA2010')

# Calculate average violent and property crime rates for 2022 for neighborhoods with universities
avg_violent_crime = merged_violent['viol21'].mean()
avg_property_crime = merged_property['prop21'].mean()
avg_all_crime = merged_all['crime21'].mean()

# Prepare data for bar chart
crime_types = ['Violent Crime', 'Property Crime', 'All Crime']
crime_rates = [avg_violent_crime, avg_property_crime, avg_all_crime]

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(crime_types, crime_rates, color=['blue', 'orange', 'green'])
plt.title('Average Crime Rates Near Universities by Crime Type (2021)', fontsize=18)
plt.xlabel('Crime Type', fontsize=14)
plt.ylabel('Average Crime Rate (Per 1,000)', fontsize=14)
plt.show()
