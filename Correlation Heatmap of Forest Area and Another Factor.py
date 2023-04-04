import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to forest area and another factor of interest
df = df[df['Indicator Code'].isin(['AG.LND.FRST.ZS', 'SP.POP.TOTL'])]
df = df[df['Country Name'].isin(['United States', 'China', 'India', 'Japan'])]

# Subset to years 1960-2020 in twenty year increments
years = list(range(1960, 2021, 20))
df = df.loc[:, ['Country Name', 'Indicator Code'] + [str(year) for year in years]]

# Pivot the data to create a multi-index DataFrame
df = df.set_index(['Country Name', 'Indicator Code']).stack().reset_index()
df.columns = ['Country', 'Indicator', 'Year', 'Value']

# Create a pivot table with values by year and indicator for each country
values_pivot = df.pivot(index=['Country', 'Year'], columns='Indicator', values='Value')

# Calculate the correlation matrix for forest area and another factor
corr_matrix = values_pivot.corr()

# Create the heatmap for forest area and another factor
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Forest Area and Another Factor')
plt.show()