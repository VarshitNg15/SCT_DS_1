import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_5871594.csv', on_bad_lines='skip')
except pd.errors.ParserError:
    print("Error reading the CSV file. Please check the file format.")
    exit()

print(df.head(4))
print(f"DataFrame shape: {df.shape}")

print(df.isnull().sum())
df = df.fillna(method="ffill")
print(df.isnull().sum())
print("Number of duplicate rows:", df.duplicated().sum())

df.drop(['Indicator Name', 'Indicator Code', 'Country Code'], axis=1, inplace=True)
print(df.columns)

df = pd.DataFrame(df)
cols = [col for col in df.columns if col != 'Country Name']

df_years = df.set_index('Country Name')
average_population_by_year = df_years.mean()

fig = plt.figure(figsize=(10, 6))
plt.hist(average_population_by_year, bins=10, color='blue', edgecolor='black')
plt.xlabel('Average Population')
plt.ylabel('Frequency')
plt.title('Histogram of Average Population by Year')
plt.show()

for i in cols:
    fig = plt.figure(figsize=(4, 3))
    plt.hist(df[i], color='blue', bins=7)
    plt.xlabel(i)
    plt.ylabel('Frequency')
    plt.title(f'Histogram for {i}')
    plt.show()

fig = plt.figure(figsize=(10, 6))
for i in cols:
    plt.hist(df[i], bins=7, alpha=0.5, label=i)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Combined Histogram for Multiple Columns')
plt.legend(loc='upper right')
plt.show()

country1960 = df.sort_values(by='1960').head(7)
print(country1960)

country1960T = country1960.set_index('Country Name').T
country2022T = df.set_index('Country Name').T

for country_name, data_values in country2022T.iterrows():
    fig = plt.figure(figsize=(30, 15))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Year')
    plt.ylabel('Data Value')
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()
