import pandas as pd
import matplotlib.pyplot as plt

# Data
university_data = pd.read_csv('Data/Universities_and_Colleges.csv')
crime_data = pd.read_csv('Data/Part_1.csv')

# Adjust
university_data['Neighborhood'] = university_data['Neighborhood'].str.upper()

# Merge data (Neighborhood column)
merged_data = pd.merge(university_data, crime_data, on='Neighborhood', how='inner')

# Group by Crime Description
crime_counts = merged_data['Description'].value_counts()

# Bar Chart
plt.figure(figsize=(12, 6))
crime_counts.plot(kind='bar', color='skyblue')
plt.title('Common Crime Near Universities', fontsize=18)
plt.xlabel('Crime Type', fontsize=14)
plt.ylabel('Crime Count', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
