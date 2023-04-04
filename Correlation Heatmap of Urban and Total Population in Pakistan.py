import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to urban population and total population data for Pakistan
df = df[df['Indicator Code'].isin(['SP.URB.TOTL', 'SP.POP.TOTL'])]
df = df[df['Country Name'] == 'Pakistan']

# Subset to years 1960-2020 in 20 year increments
years = list(range(1960, 2021, 20))
df = df.loc[:, ['Indicator Code'] + [str(year) for year in years]]

# Pivot the data to create a multi-index DataFrame
df = df.set_index(['Indicator Code']).stack().reset_index()
df.columns = ['Indicator', 'Year', 'Population']

# Create a pivot table with population by year and indicator
pop_pivot = df.pivot(index='Year', columns='Indicator', values='Population')

# Calculate the correlation matrix
corr_matrix = pop_pivot.corr()

# Create the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Urban and Total Population in Pakistan')
plt.show()
