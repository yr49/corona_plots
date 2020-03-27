# -*- coding: utf-8 -*-
"""
Created by: Yaniv Ravid

Import dependencies: `pandas` & `pyplot`. Build dataframes from NYT github repositories.
"""

import pandas as pd
from matplotlib import pyplot as plt
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df1 = pd.read_csv(url, error_bad_lines=False)
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df2 = pd.read_csv(url, error_bad_lines=False)

"""Plot case number and death count for specific state. Change string variable `state` to your state of interest."""

state = "New Mexico"
df_state = df.loc[df['state'] == state]
dates = df_state['date'].values
dates = [i[6:] for i in dates]
plt.figure(figsize=(12,5))
plt.plot(dates, df_state['cases'], c='r')
plt.xticks(rotation=90)
plt.title("Number of cases in " + state + " state")
plt.grid(True)
plt.show()
plt.figure(figsize=(12,5))
plt.plot(dates, df_state['deaths'])
plt.xticks(rotation=90)
plt.title("Number of deaths in " + state + " state")
plt.grid(True)
plt.show()

"""Plot case number and death count for specific county. Change string variables `county` and `state` to your county of interest and its respoective state."""

county = 'Los Angeles'
state = 'California'
df_county = df2.loc[df2['state'] == state]
df_county = df_county.loc[df_county['county'] == county]
dates = df_county['date'].values
dates = [i[6:] for i in dates]
plt.figure(figsize=(12,5))
plt.plot(dates, df_county['cases'], c='r')
plt.xticks(rotation=90)
plt.title("Number of cases in " + county + ", " + state)
plt.grid(True)
plt.show()
plt.figure(figsize=(12,5))
plt.plot(dates, df_county['deaths'])
plt.xticks(rotation=90)
plt.title("Number of deaths in " + county + ", " + state)
plt.grid(True)
plt.show()