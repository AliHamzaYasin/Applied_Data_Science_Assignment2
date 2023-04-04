import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)

# Subset to the indicators of interest
df = df[df['Indicator Code'].isin(['SP.URB.TOTL', 'SP.RUR.TOTL', 'AG.LND.FRST.K2', 'AG.LND.ARBL.HA', 'NY.GDP.MKTP.CD', 'EN.ATM.GHGT.KT.CE', 'EG.USE.COMM.GD.PP.KD'])]

# Subset to Pakistan and years 1960-2020 in 20 year increments
years = list(range(1960, 2021, 20))
df = df.loc[df['Country Code']=='PAK', ['Indicator Code'] + [str(year) for year in years]]

# Pivot the data to create a multi-index DataFrame
df = df.set_index('Indicator Code').stack().reset_index()
df.columns = ['Indicator', 'Year', 'Value']

# Create a pivot table with values by year and indicator
values_pivot = df.pivot(index='Year', columns='Indicator', values='Value')

# Calculate the correlation matrix
corr_matrix = values_pivot.corr()

# Create the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Pakistan')
plt.show()
