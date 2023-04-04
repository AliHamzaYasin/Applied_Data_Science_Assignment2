import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and subset to relevant indicators and countries
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)
df = df[df['Indicator Code'] == 'EN.ATM.GHGT.KT.CE']
countries = ['United States', 'China', 'India', 'Japan', 'South Korea', 'Indonesia']
df = df[df['Country Name'].isin(countries)]

# Subset to years 1990-2020 in five year increments
years = [str(year) for year in range(1990, 2021, 5)]
df = df.loc[:, ['Country Name'] + years]

# Pivot the data to create a multi-index DataFrame
df = df.set_index('Country Name').stack().reset_index()
df.columns = ['Country', 'Year', 'Value']
df = df.pivot(index='Year', columns='Country', values='Value')

# Plot the line graph
ax = df.plot(kind='line', figsize=(10,6))
ax.set_xlabel('Year')
ax.set_ylabel('Greenhouse Gas Emissions (kt of CO2 equivalent)')
ax.set_title('Greenhouse Gas Emissions by Country (1990-2020)')
plt.show()