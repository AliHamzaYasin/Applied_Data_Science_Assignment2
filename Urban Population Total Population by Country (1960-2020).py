import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to urban population and total population data
df = df[df['Indicator Code'].isin(['SP.URB.TOTL', 'SP.POP.TOTL'])]
df = df[df['Country Name'].isin(['United States', 'China', 'Pakistan', 'Russian Federation'])]

# Subset to years 1960-2020 in twenty year increments
years = list(range(1960, 2021, 20))
df = df.loc[:, ['Country Name', 'Indicator Code'] + [str(year) for year in years]]

# Pivot the data to create a multi-index DataFrame
df = df.set_index(['Country Name', 'Indicator Code']).stack().reset_index()
df.columns = ['Country', 'Indicator', 'Year', 'Population']

# Create a bar graph for each indicator and country
for indicator in ['SP.URB.TOTL', 'SP.POP.TOTL']:
    sns.catplot(data=df[df['Indicator'] == indicator], x='Year', y='Population', hue='Country',
                kind='bar', height=5, aspect=2)
plt.title('Urban Population V/s Total Population by Country (1960-2020)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
