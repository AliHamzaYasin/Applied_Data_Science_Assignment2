import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Select relevant indicators and countries
indicators = ['EG.USE.PCAP.KG.OE']
countries = ['United Arab Emirates', 'Qatar', 'Bahrain', 'Iran, Islamic Rep.', 'Pakistan','China', 'India']

# Subset the data
df = df[df['Indicator Code'].isin(indicators) & df['Country Name'].isin(countries)]
years = [str(year) for year in range(1990, 2015)]
df = df[['Country Name'] + years]  # Include relevant columns

# Pivot the data to create a multi-index DataFrame
df = df.set_index('Country Name').stack().reset_index()
df.columns = ['Country', 'Year', 'Energy Consumption']

# Plot the line graph for the selected countries
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Energy Consumption', hue='Country')
plt.title('Energy Consumption by Country (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Kg of oil equivalent per capita')
plt.show()
