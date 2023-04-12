import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df_meth = pd.read_csv("methane.csv")
df_meth.drop(columns='source')
df_meth.shape

#Data by country and type
grouped_data = df_meth.groupby(['country', 'type']).agg({'emissions': 'sum'}).reset_index()

# Sort the grouped data by emissions in descending order to get the top 10 countries
top_countries_data = grouped_data.groupby('country').agg({'emissions': 'sum'}).sort_values(by='emissions', ascending=False).head(10).reset_index()
top_countries = top_countries_data['country'].tolist()
top_grouped_data = grouped_data[grouped_data['country'].isin(top_countries)]

# Create a stacked bar chart for the top 10 countries, broken down by type
fig, ax = plt.subplots(figsize=(12, 6))
top_grouped_data.pivot_table(values='emissions', index='country', columns='type', aggfunc='sum').loc[top_countries].plot(kind='bar', stacked=True, ax=ax)
plt.title('Top 10 Countries by Methane Emissions - Type-wise')
plt.xlabel('Country')
plt.ylabel('Emissions')
plt.legend(title='Type', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.show()



df_oil_gas =  pd.read_csv("oil_gas.csv")
df_coal = pd.read_csv("coal.csv")
df_abat = pd.concat([df_oil_gas, df_coal])
df2=df_abat.drop(["source"], axis=1)

# Grouping data by type to get the mean savings and cost
abatement_grouped = df2.groupby('type').agg({'savings': 'mean', 'cost': 'mean'}).reset_index()

# savings-to-cost ratio
abatement_grouped['savings_to_cost_ratio'] = abatement_grouped['savings'] / abatement_grouped['cost']

# savings-to-cost ratio in descending order
sorted_data = abatement_grouped.sort_values(by='savings_to_cost_ratio', ascending=False)
print(sorted_data)

# graph to visualize
fig, ax = plt.subplots(figsize=(12, 6))
sorted_data.plot(x='type', y='savings_to_cost_ratio', kind='bar', ax=ax, legend=None, color= ['blue', 'orange','red'])
# graph labels and title
plt.xlabel('Abatement Type')
plt.ylabel('Savings-to-Cost Ratio')
plt.title('Effectiveness of Abatement Types')
# plt.xticks(rotation=75)
plt.show()









