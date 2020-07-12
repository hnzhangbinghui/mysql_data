##https://blog.csdn.net/qq_39314932/article/details/96180914
import xlrd
import os
filename="Lenovo.xlsx"
filepath=os.path.join(os.getcwd(),filename)
print(filepath)
#打开并读取excle文件信息；
excel_file=xlrd.open_workbook(filepath) #打开excel文件；
sheet1=excel_file.sheet_by_index(0) #根据sheet页的排序选取sheet
row_content=sheet1.row_values(0) #获取指定行的数据，返回列表，排序从0开始，获取第一列的字段信息；
print(row_content)
print("获取所有sheet名字：",excel_file.sheet_names())
print("获取sheet的数量：",excel_file.nsheets)
print("获取所有sheet对象",excel_file.sheets())
print("通过sheet名查找对应的sheet",excel_file.sheet_by_name("test_sheet"))
print("******************************")
print("获取所有的行数：",sheet1.nrows)
print("获取所有的列数：",sheet1.ncols)
print(" 获取单元格值类型和内容：",sheet1.row(0))
print("获取单元格数据类型：",sheet1.row_types(0))
print("******************************")
#表操作
print("获取第1行的第6-10列的值，不包括第10列：",sheet1.row_values(0,6,10))
print("获取第一列，第0-5行的值，不包括第5行：",sheet1.col_values(0,0,5))
print("获取第6列的所有的值：",sheet1.col_values(6,1))
six_col=sheet1.col_values(6,1)
print(six_col)
print(len(six_col))
print("******************************")
#获取特定单元格的值和类型
print("获取第20行第一列的值：",sheet1.cell_value(19,0))
print("获取第20行第一列的值：",sheet1.cell(19,0).value)
print("获取第20行第一列的值：",sheet1.row(19)[0].value)
print("获取第20行第一列的单元格的类型：",sheet1.cell_type(19,0))
print("获取第20行第一列的单元格的类型：",sheet1.cell(19,0).ctype)
print("获取第20行第一列的单元格的类型：",sheet1.row(19)[0].ctype)
print("******************************")
#(0,0)转换A1
print("(0,0)转换A1:",xlrd.cellname(0,0))
print("(0,0)转换A1:",xlrd.cellnameabs(0,0))
print("(0,0)转换A1:",xlrd.colname(509))
'''数据类型：
空：0
字符串：1
数字：2
日期：3
布尔：4
error：5
'''







