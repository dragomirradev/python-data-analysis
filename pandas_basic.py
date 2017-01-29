# coding: utf-8
import pandas as pd

# Some basic data
a = { 'name': 'John', 'age': 29, 'id': 1 }
b = { 'name': 'Doe', 'age': 19, 'id': 2 }
c = [ a, b ] 
c

# Using the above data as Foreign Key (FK)
p = { 'user_id': 1, 'likes': 'Mango' }
q = { 'user_id': 1, 'likes': 'Pepsi' }
r = { 'user_id': 2, 'likes': 'Burger' }
s = [ p, q, r ]

# Create Pandas DataFrame object and set
# appropriate index
df1 = pd.DataFrame(c)
df1.set_index('id')
df1

df2 = pd.DataFrame(s)
df2.set_index('user_id')
df2

# Using the FK relation to create a join
pd.merge(df1, df2, left_on='id', right_on='user_id')
m = pd.merge(df1, df2, left_on='id', right_on='user_id')
m.set_index('user_id')

# Basic aggregate operations
m.groupby('likes')
m.groupby('likes')['likes'].count()
