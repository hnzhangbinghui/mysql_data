
import xlrd
import pymysql
#打开excel表
def open_excel():
    try:
        book=xlrd.open_workbook(r'E:\Api_Auto_Test\Data analysis\user.xlsx')
    except:
        print("Open excel file failed!!")
    try:
        sheet=book.sheet_by_index(0)
        return sheet
    except:
        print("Locate worksheet in excel failed!!")
#链接数据库
try:
    db=pymysql.connect(host="127.0.0.1",user='root',password='zbh123456',database='world')
except:
    print("Could not connect to mysql server!!")
def search_count():
    cursor=db.cursor()
    select="select count(ID) from zhang_user"
    cursor.execute(select) #执行sql语句
    line_count=cursor.fetchone()
    print(line_count[0])

def insert_data():
    sheet=open_excel()
    cursor=db.cursor()
    for i in range(1,sheet.nrows): #第一行是标题名，对应表中的字段应该是从第二行开始；
        name=sheet.cell(i,0).value  #获取第i行第0列；
        age=sheet.cell(i,1).value
        print("第i行第0列的值：",name)
        print("第i行第1列的值：",age)
        value=(name,age)
        print(value)
        sql="INSERT INTO world.zhang_user(name,age)VALUES(%s,%s)"
        cursor.execute(sql,value)
        db.commit()
    cursor.close()  #关闭连接

#执行insert_data函数
insert_data()
db.close() #关闭数据
print("插入数据完成；")


