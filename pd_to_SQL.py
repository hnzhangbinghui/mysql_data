import pymysql
import sklearn
from sklearn import *
import pandas as pd
# from pandas import read_sql

conn = pymysql.connect(host='127.0.0.1', database='world', user='root', password='zbh123456', port=3306)
sql = "select * from city"
df_iris=pd.read_sql(sql,conn)
print(df_iris)
print(type(df_iris))
print(df_iris.head())
print(df_iris.tail())
print('****************************')
print(df_iris.info())
print('****************************')
print(df_iris.describe())
print(df_iris.describe(include=['O']).T)

print('****************************')
import seaborn as sns
import matplotlib

df_iris.Species.value_counts()





