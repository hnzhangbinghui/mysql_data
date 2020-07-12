# https://blog.csdn.net/weixin_38546295/article/details/83537558
'''pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None,
              usecols=None, squeeze=False,dtype=None, engine=None,
              converters=None, true_values=None, false_values=None,
              skiprows=None, nrows=None, na_values=None, parse_dates=False,
              date_parser=None, thousands=None, comment=None, skipfooter=0,
              convert_float=True, **kwds)'''
# pandas读取excel后返回的是dataframe
import pandas as pd

# 1
io = r'D:\Api_Auto_Test\Didi\Test_excel.xlsx'
data = pd.read_excel(io, sheet_name=0)
# 可以用整形数字，列表名和sheetN来的到对应的sheet；sheet的名字从0开始，读取相应的sheet；
# sheet_name=[0,'name','Sheet4'],可以等于列表，代表读取三个工作表；sheet_name,默认是0，读取第一个sheet；
print('得到sheet的前五行数据：\n', data.head())
data1 = pd.read_excel(io, sheet_name=0, nrows=8)
print('读取指定行数的记录：\n', data1)
print("*******************************")
# 2,header,用哪一行作列名，默认是0，如果设置为[0,1]，则表示用前两行作为多重索引
data2 = pd.read_excel(io, sheet_name=0, header=[0, 1], nrows=5)  # 用前两行作为索引，并取前五行记录；
print('多重索引：\n', data2)
print("*******************************")
# 3,names,自定义最终的列名，可以对于缺少或者需要重命名的列名进行设置；注意names的长度必须和excel表的列长度一致；
data3 = pd.read_excel(io, sheet_name=0, nrows=8, names=['ID', '姓名', '国籍', '其他', '数量'])
print(data3)

# 4,index_col,设置用作索引的列，index_col=可以是：列名称，整型或者整型列表（0，[0,1]）,如果选择多个列，则返回多重索引
data4 = pd.read_excel(io, sheet_name=0, nrows=8, names=['ID', '姓名', '国籍', '其他', '数量'],
                      index_col='数量')
print(data4)
# 多重索引
data5 = pd.read_excel(io, sheet_name=0, nrows=8, names=['ID', '姓名', '国籍', '其他', '数量'],
                      index_col=[0, 4])
print(data5)
print('*****************************')
# 5、usecols，需要读取的那些列，可以使用整型；
# 可以使用Excel传统的列名“A”、“B”等字母，如“A：C, E” ="A, B, C, E"，注意两边都包括。
# usecols 可避免读取全量数据，而是以分析需求为导向选择特定数据，可以大幅提高效率。
print('&&&&&&&&&&&&&&&&&&&&&&&&&')
data6 = pd.read_excel(io, sheet_name=0, nrows=8, usecols=[0, 1, 4])
print(data6)
data6 = pd.read_excel(io, sheet_name=0, nrows=8, usecols="A,B,C")
print('得到指定列的值:\n', data6)

# 6、squeeze,当数据仅包含一列；squeeze为True时，返回series，否则返回dataframe；
data7 = pd.read_excel(io, sheet_name=0, nrows=8, usecols='C', squeeze=True)
print(type(data7), '\n', data7)
data7 = pd.read_excel(io, sheet_name=0, nrows=8, usecols='C', squeeze=False)
print(type(data7), '\n', data7)

# 7,converters，强制规定列数据类型，主要是保留以文本形式存储的数字；
# converters={'排名':'str','场次':'int'},将数据类型强制规定为字符串，
# pandas默认是将文本类的数据读取为整型；‘场次’列强制规定为整型；
print('%%%%%%%%%%%%%%%%%%%%%%%%')
print('未转化之前的类型：',data['Population'].dtype)
data8=pd.read_excel(io,sheet_name=0,converters={'Population':str})
print('转化后的类型：',data8['Population'].dtype)

#8,skiprows，跳过特定行，skiprows=N,跳过前N行；skiprows=[a,b,c],跳过a+1,b+1,c+1,行，索引从0开始；
#使用skiprows后，有可能首行也会被跳过；
data8= pd.read_excel(io, sheet_name=0, skiprows=2) #把列名也跳过了；
print(data8)
data8= pd.read_excel(io, sheet_name=0, skiprows=[1,3,5]) #跳过指定的行
print(data8)
#9、skipfooter,跳过末尾N行
data8= pd.read_excel(io, sheet_name=0, skipfooter=6) #跳过末尾6行；
print(data8)
















