import pandas as pd
from matplotlib import pyplot as plt
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df1 = pd.read_csv(url, error_bad_lines=False)
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df2 = pd.read_csv(url, error_bad_lines=False)

"""Plot case number and death count for specific state. Change string variable `state` to your state of interest."""

def plot_state(state):
  '''
  Generates two plots: number of cases vs. date, number of deaths vs. date

  Parameters: `state` (string)

  Example: plot_state('New York')
  '''
  df_state = df1.loc[df1['state'] == state]
  dates = df_state['date'].values
  dates = [i[6:] for i in dates]
  plt.figure(figsize=(15,5))
  plt.plot(dates, df_state['cases'], c='r')
  plt.xticks(rotation=90)
  plt.title("Number of cases in " + state + " state")
  plt.grid(True)
  plt.show()
  plt.figure(figsize=(15,5))
  plt.plot(dates, df_state['deaths'])
  plt.xticks(rotation=90)
  plt.title("Number of deaths in " + state + " state")
  plt.grid(True)
  plt.show()

def plot_state_new(state):
  '''
  Generates two plots: number of new cases vs. date, number of new deaths vs. date

  Parameters: `state` (string)

  Example: plot_state_new('New York')
  '''
  df_state = df1.loc[df1['state'] == state]
  dates = df_state['date'].values
  dates = [i[6:] for i in dates]
  new_cases = [0]
  for i in range(1, len(df_state['cases'])):
    new_cases.append(df_state['cases'].values[i] - df_state['cases'].values[i-1])
  new_deaths = [0]
  for i in range(1, len(df_state['deaths'])):
    new_deaths.append(df_state['deaths'].values[i] - df_state['deaths'].values[i-1])
  plt.figure(figsize=(15,5))
  plt.plot(dates, new_cases, c='r')
  plt.xticks(rotation=90)
  plt.title("Number of new cases in " + state + " state")
  plt.grid(True)
  plt.show()
  plt.figure(figsize=(15,5))
  plt.plot(dates, new_deaths)
  plt.xticks(rotation=90)
  plt.title("Number of new deaths in " + state + " state")
  plt.grid(True)
  plt.show()

"""Plot case number and death count for specific county. Change string variables `county` and `state` to your county of interest and its respoective state."""

def plot_county(county, state):
  '''
  Generates two plots: number of cases vs. date, number of deaths vs. date

  Parameters: `county` (string), `state` (string)

  Example: plot_county('New York City', 'New York')
  '''
  df_county = df2.loc[df2['state'] == state]
  df_county = df_county.loc[df_county['county'] == county]
  dates = df_county['date'].values
  dates = [i[6:] for i in dates]
  plt.figure(figsize=(15,5))
  plt.plot(dates, df_county['cases'], c='r')
  plt.xticks(rotation=90)
  plt.title("Number of cases in " + county + ", " + state)
  plt.grid(True)
  plt.show()
  plt.figure(figsize=(15,5))
  plt.plot(dates, df_county['deaths'])
  plt.xticks(rotation=90)
  plt.title("Number of deaths in " + county + ", " + state)
  plt.grid(True)
  plt.show()

def plot_county_new(county, state):
  '''
  Generates two plots: number of cases vs. date, number of deaths vs. date

  Parameters: `county` (string), `state` (string)

  Example: plot_county('New York City', 'New York')
  '''
  df_county = df2.loc[df2['state'] == state]
  df_county = df_county.loc[df_county['county'] == county]
  dates = df_county['date'].values
  dates = [i[6:] for i in dates]
  new_cases = [0]
  for i in range(1, len(df_county['cases'])):
    new_cases.append(df_county['cases'].values[i] - df_county['cases'].values[i-1])
  new_deaths = [0]
  for i in range(1, len(df_county['deaths'])):
    new_deaths.append(df_county['deaths'].values[i] - df_county['deaths'].values[i-1])
  plt.figure(figsize=(15,5))
  plt.plot(dates, new_cases, c='r')
  plt.xticks(rotation=90)
  plt.title("Number of new cases in " + county + ", " + state)
  plt.grid(True)
  plt.show()
  plt.figure(figsize=(15,5))
  plt.plot(dates, new_deaths)
  plt.xticks(rotation=90)
  plt.title("Number of new deaths in " + county + ", " + state)
  plt.grid(True)
  plt.show()

plot_state_new('Connecticut')

plot_county_new("Miami-Dade", "Florida")
