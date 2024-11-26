import pandas as pd
import matplotlib.pyplot as plt

# Data
liquor_data = pd.read_csv(('Data/Liquor_Outlets_Density.csv'))
crime_data = pd.read_csv('Data/Part_1.csv')

# Adjust
liquor_data['Neighborhood'] = liquor_data['Neighborhood'].str.upper()

# Merge data 
merged_data = pd.merge(liquor_data, crime_data, on='Neighborhood', how="inner")

# Group by Crime Description
crime_counts = merged_data['Description'].value_counts()

# Bar Chart
plt.figure(figsize=(12, 6))
crime_counts.plot(kind='bar', color='skyblue')
plt.title('Common Crime Near Liquor Stores', fontsize=18)
plt.xlabel('Crime Type', fontsize=14)
plt.ylabel('Crime Count', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()