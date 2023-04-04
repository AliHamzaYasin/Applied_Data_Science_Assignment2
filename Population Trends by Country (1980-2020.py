import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to population data
df = df[df['Indicator Code'] == 'SP.POP.TOTL']
df = df[df['Country Name'].isin(['United States', 'China', 'India', 'Japan','Pakistan'])]

# Subset to years 1990-2020 in five year increments
years = [str(year) for year in range(1980, 2021, 5)]
df = df.loc[:, ['Country Name'] + years]

# Pivot the data to create a multi-index DataFrame
df = df.set_index('Country Name').stack().reset_index()
df.columns = ['Country', 'Year', 'Population']

# Create a line graph for each country
fig, ax = plt.subplots(figsize=(10, 6))
for country in ['United States', 'China', 'India', 'Japan']:
    country_data = df[df['Country'] == country]
    ax.plot(country_data['Year'], country_data['Population'], label=country)

ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title('Population Trends by Country (1980-2020)')
ax.legend()
plt.show()
