import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to urban population and total population indicators
df = df[df['Indicator Code'].isin(['SP.URB.TOTL', 'SP.POP.TOTL'])]

# Subset to Pakistan, India, China, and Bangladesh
df = df[df['Country Code'].isin(['PAK', 'IND', 'CHN', 'BGD'])]

# Subset to years 1960-2020 in 20 year increments
years = list(range(1960, 2021, 20))
df = df.loc[:, ['Country Code', 'Indicator Code'] + [str(year) for year in years]]

# Pivot the data to create a multi-index DataFrame
df = df.set_index(['Country Code', 'Indicator Code']).stack().reset_index()
df.columns = ['Country', 'Indicator', 'Year', 'Value']

# Create a pivot table with values by year and indicator for each country
values_pivot = df.pivot(index=['Country', 'Year'], columns='Indicator', values='Value')

# Calculate the correlation matrix
corr_matrix = values_pivot.corr()

# Create the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Urban and Total Population')
plt.show()
