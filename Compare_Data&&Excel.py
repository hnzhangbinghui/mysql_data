import xlrd
import os
import pymysql
def Open_excel():
    filename="Lenovo.xlsx"
    filepath=os.path.join(os.getcwd(),filename)
    excel_file=xlrd.open_workbook(filepath)
    sheet=excel_file.sheet_by_index(0)
    targets_excel=sheet.col_values(6,1)
    return targets_excel
def Open_data():
    conn=pymysql.connect(host='127.0.0.1',user='root',passwd='zbh123456',port=3306,database='world')
    cur=conn.cursor()
    sql='SELECT * FROM zhang_lenovo'
    count=cur.execute(sql)
    all_data=cur.fetchall()
    targets_data=[]
    for i in range(count):
        targets_data.append(int(all_data[i][6]))
    return targets_data
def Open_incentiveID(x):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='zbh123456',port=3306,database='world')
    cur = conn.cursor()
    sql = 'SELECT * FROM zhang_lenovo'
    count = cur.execute(sql)
    assert_data = cur.fetchall()
    print("该incentiveID的值是：",assert_data[x][3])
def Compare_data():
    tar_excel=Open_excel()
    tar_data=Open_data()
    for i in range(len(tar_excel)):
        if tar_excel[i]==tar_data[i]:
            print("Calculation rasult is True!!")
        else:
            Open_incentiveID(i)
            print("数据库的值是：",tar_data[i]," " ,"excel表格的值是：",tar_excel[i])
if __name__=="__main__":
    Compare_data()
