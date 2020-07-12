
#https://www.cnblogs.com/QingXiaxu/p/8377955.html
import pymysql
#链接数据库
conn=pymysql.connect(host="127.0.0.1",user='root',password='zbh123456',database='world',port=3306)
cur=conn.cursor()
sql="SELECT * FROM zhang_lenovo"
cur.execute(sql)
count=cur.execute("select * from zhang_lenovo where id>=364")
print(count)
print("**************************")
users=cur.fetchall()
print(users)  #每一行的所有元素是一个元祖
print(len(users)) #得到的是该表的总行数
'''print("**************************")
for i in range(count):  #依次读取数据库的每一行数据；
    result=cur.fetchone()
    if result[6] in ('3677900','11'):
        print(result[0])
    else:
        print("比对失败")'''
'''print("**************************")
user2=cur.fetchmany(20)   #获取指定行数的列表数据：
print(user2[0][0])'''
#把得到的二维元祖转化为二维列表；
users_list=[]
for i in range(len(users)):
    users_list.append(list(users[i]))
print(users_list)
print("**************************")
#得到数据库列表当中的某一个值
targets=[]
for i in range(len(users_list)):
    targets.append(users_list[i][6])
print(targets)
print("**************************")
#从excel表中抓取相应列的值：
import xlrd
import os
#book = xlrd.open_workbook(r'E:\Api_Auto_Test\Data analysis\Lenovo.xlsx')
#sheet=book.sheet_by_index(0)
filename="Lenovo.xlsx"
filepath=os.path.join(os.getcwd(),filename)
print(filepath)
