import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates
register_matplotlib_converters()

# Connect quandl and grab data
quandl.ApiConfig.api_key = 'A2hfPPx7xtRt9nMCJusn'
apple = quandl.get('EOD/AAPL')

# Define axis values
x = (apple.index - apple.index[0]).days
y = apple['Adj_Close'].values

# Regression method by Statsmodels
x1 = sm.add_constant(x)
result = sm.OLS(y,x1).fit()
print(result.summary())

# Regression method by sklearn
x = np.array(x).reshape(-1,1)
y = y.reshape(-1,1)
Lr = LinearRegression()
Lr.fit(x,y)

# Setting x axis tick labels
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

# Plotting
fig, ax = plt.subplots()
ax.plot(apple.index, apple['Adj_Close'], label='APPL')
ax.plot(apple.index, Lr.predict(x), 'r--', label='Linear Reg.')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_minor_locator(months)
ax.xaxis.set_major_formatter(years_fmt)
ax.set_ylabel('Price ($)')
ax.set_title('Date vs Price')

plt.legend()
plt.show()
