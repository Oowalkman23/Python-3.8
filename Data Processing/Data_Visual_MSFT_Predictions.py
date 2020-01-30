import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import quandl
import seaborn as sbn
import statsmodels.api as sm
import matplotlib.dates as mdates
register_matplotlib_converters()

# Setting for x axis tick labels
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

quandl.ApiConfig.api_key = 'A2hfPPx7xtRt9nMCJusn'
microsoft = quandl.get('EOD/MSFT')

# Check Initial Stock Price Chart 
'''
fig, ax = plt.subplots()
ax.plot(microsoft.index, microsoft['Adj_Close'])
ax.set_ylabel('Price ($)')
ax.set_title('Stock Price Microsoft')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
plt.grid(which='major', axis='both', color='k', linestyle='--', linewidth=0.25)
plt.show()
'''

# Checking for the distribution of Adj_Close
'''
plt.figure(figsize=(5,3))
plt.tight_layout()
sbn.distplot(microsoft['Adj_Close'])
plt.show()
'''

#Numpy array conversion from Pandas core dataframe
x = np.array((microsoft.index - microsoft.index[0]).days)
y = np.array(microsoft['Adj_Close'])

# Statmodels regression method
x1 = x.copy()
x1 = sm.add_constant(x1)
result = sm.OLS(y, x1).fit()
summary = result.summary()
# print(summary)

# Reshape to 2D array
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
# sklearn regression method
Lr = LinearRegression()
Lr.fit(x, y)

# Stock Price Chart with univariate regression line
'''
fig, ax = plt.subplots()
ax.plot(microsoft.index, Lr.predict(x), 'r--', label='Regressor')
ax.plot(microsoft.index, microsoft['Adj_Close'], label='MSFT')
ax.set_title('Microsoft Stock Price')
ax.set_ylabel('Price ($)')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
plt.grid(which='major', linestyle='--', linewidth='0.25')
plt.legend()
plt.show()
'''

# Split x and y into test and train, for later prediction by regression
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# New regressor line with train samples
regressor = LinearRegression()
regressor.fit(x_train, y_train)
# Value of const. and x coefficient
'''
print(regressor.intercept_)
print(regressor.coef_)
'''

# Prediction data
y_pred = regressor.predict(x_test)
# Prediction - Actual database
datares = pd.DataFrame({'Actual':y_test.flatten(), 'Prediction':y_pred.flatten()})
datares['Error'] = 0
# Set error values
for i in range(len(datares['Error'])):
    datares.loc[i, 'Error'] = (round((abs(datares.loc[i, 'Actual'] - datares.loc[i, 'Prediction']) / datares.loc[i, 'Actual']), 2) * 100)

# Scatter plot for error
fig, ax = plt.subplots()
ax.scatter(datares.index, datares['Error'])
ax.set_ylabel('Error %')
ax.set_xlabel('Data -n')
ax.set_title('Prediction Error')
plt.grid(linestyle='--', linewidth=0.25)
plt.show()

# Mean Absolute Error
print('The Mean Absolute Error =', metrics.mean_absolute_error(y_test, y_pred), end='\n')

# Mean Squared Error
print('The Mean Squared Error =', metrics.mean_squared_error(y_test, y_pred), end='\n')

# Root Mean Squared Error
print('The Root Mean Squared Error =', np.sqrt(metrics.mean_squared_error(y_test, y_pred)), end='\n')



'''
Reference(s) in making this:
a. github.com/WillKoehrsen
b. towardsdatascience.com
c. geeksforgeeks.org
d. stackoverflow.com

More quantitative analysis coming up..
'''
