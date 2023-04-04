# Summary statistics for each country


import pandas as pd

#Datafilename = r'H:\dataset\WorldBank\API_19_DS2_en_csv_v2_5361599.csv'
dataset = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Print out the unique values of the 'Indicator Code' column
print(dataset['Indicator Name'].unique())

# Define the indicators and countries of interest
indicators = ['Urban population', 'Population, total']
countries = ['United States', 'China', 'India']

# Check if the specified indicators are present in the dataset
if not set(indicators).issubset(set(dataset['Indicator Name'].unique())):
    raise ValueError("Specified indicators are not present in the dataset")

# Subset the data for the indicators and countries of interest
sub_set = dataset[(dataset['Country Name'].isin(countries)) & (dataset['Indicator Name'].isin(indicators))]
sub_set = sub_set[['Country Name', 'Indicator Name', '2019']]

# Rename columns to match indicators
sub_set = sub_set.rename(columns={'Indicator Name': 'Indicator', '2019': 'Value'})

# Pivot the data to create separate columns for each indicator
sub_set = sub_set.pivot(index='Country Name', columns='Indicator', values='Value')

# Compute summary statistics for the whole world
world_stats = sub_set.describe()

# Compute summary statistics for each country
country_stats = sub_set.describe()

# Print the summary statistics
print("Summary statistics for the whole world:")
print(world_stats)

print("\nSummary statistics for each country:")
print(country_stats)

