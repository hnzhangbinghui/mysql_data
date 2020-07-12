import pandas as pd

# 生成dataframe的数据
io = r'D:\Api_Auto_Test\Didi\Test_excel.xlsx'
df = pd.read_excel(io, sheet_name=0)
# print(df)

# 1、把数据写入csv文件
df.to_csv('df_csv.csv', sep=',', header=True, index=True)
# 2、把数据写入json文件
df_json = df.to_json('df_json.json')
import json
json_test=pd.read_json('df_json.json')
print(json_test.values.tolist())
# 3、把数据写入html文件
df.to_html('df_html.html')
# 4、把数据写入剪贴板中
a = df.to_clipboard()
# 4、写入到数据库（重点）
import pymysql
from sqlalchemy import create_engine

connect = create_engine('mysql+pymysql://root:zbh123456@localhost:3306/world?charset=utf8mb4')
# connect = create_engine('mysql+pymysql://root:zbh123456@localhost:3306/world?',encoding='utf-8')

pd.io.sql.to_sql(df, 'city1', connect, if_exists='replace', schema='world')
# if_exists,等于append，追加到数据库下面；等于replace,‘replace’表示如果同名表存在就替换掉
