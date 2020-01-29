import psycopg2 as ps
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ColorConverter
import numpy as np

#Connect postgresql
conn = ps.connect(user = 'postgres_user',
                  host = 'localhost',
                  port = '5432',
                  database = 'database_name',
                  password = 'password')
#Cursor assignment
cur = conn.cursor()

#Grab sample data
dataTable = "SELECT * FROM public.sales_by_film_category"
cur.execute(dataTable)
data = cur.fetchall()

#Get column name
column_name = [col[0] for col in cur.description]
print(column_name)
#Result column_name:
# ['category', 'total_sales']

#Converting to pandas dataframe 
data_pandas = pd.DataFrame(data)
data_pandas.columns = column_name
print(data_pandas)
#Result data_pandas:
#       category    total_sales
#0        Sports     4892.19
#1        Sci-Fi     4336.01
#2     Animation     4245.31
#     ------and so forth------

#Set axes by converting it first to numpy array
x = np.array([data_pandas[column_name[0]][i] for i in range(len(data_pandas[column_name[0]]))])
y = np.array([int(data_pandas[column_name[1]][i]) for i in range(len(data_pandas[column_name[1]]))])
print(x, '\n', y)
#Result x:
# ['Sports' 'Sci-Fi' 'Animation' 'Drama' 'Comedy' 'New' 'Action' 'Foreign'
#  'Games' 'Family' 'Documentary' 'Horror' 'Classics' 'Children' 'Travel'
#  'Music']

#Result y:
# [4892 4336 4245 4118 4002 3966 3951 3934 3922 3830 3749 3401 3353 3309
#  3227 3071]

#Setting for visualization
fig = plt.figure(figsize=(9,9))
d1 = fig.add_subplot(111, xlabel='Category', ylabel='Total Sales ($)')
d1.set_title('Chart Sales by Film Category')

#Add annotation to each data
for i,j in zip(x,y):
    d1.annotate(str(j), xy=(i,j+30))

#Example of color conversion tuple float RGBA
color_black = ColorConverter().to_rgba('black')
color_cyan = ColorConverter().to_rgba('cyan')

#Visualize plot in bar chart, color cyan
d1.bar(x, y, width=0.5, color=color_cyan)
plt.show()

#Close connection
cur.close()
conn.close()