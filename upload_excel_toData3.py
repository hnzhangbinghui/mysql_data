
import xlrd
import pymysql
#打开excel表
def open_excel():
    try:
        book=xlrd.open_workbook(r'E:\Api_Auto_Test\Data analysis\Lenovo.xlsx')
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
    select="select count(*) from zhang_lenovo"
    cursor.execute(select) #执行sql语句
    line_count=cursor.fetchone()
    print(line_count[0])

def insert_data():
    sheet=open_excel()
    cursor=db.cursor()
    for i in range(1,sheet.nrows): #第一行是标题名，对应表中的字段应该是从第二行开始；
        row_data=sheet.row_values(i)  #获取改行的所有值
        value=(row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7],row_data[8],row_data[9],row_data[10],row_data[11],row_data[12])
        print("第",i,"行的值：",value)
        sql = "INSERT INTO world.zhang_lenovo(id,calculation_id,market,incentive_id,incentive_name,pep_element,target,cdi_month,achievement,achievementpctg,name,name2,name3)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,value)
        db.commit()
    cursor.close()  #关闭连接

#执行insert_data函数
insert_data()
db.close() #关闭数据
print("插入数据完成；")
