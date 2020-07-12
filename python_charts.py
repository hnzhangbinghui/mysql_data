import pyecharts

'''说到 pyecharts 要先提到它的前身 ECharts, ECharts是由百度开源的一款使用 JavaScript 实现的开源可视化库，涵盖了各种图表、
满足各类业务需求，现在已经命名为Apache ECharts(由Apache基金会接管)。
而 pyecharts 就是 ECharts 在Python中的实现，其核心原理主要是写了一个Python的库，封装了ECharts各类图表的基本操作，
然后通过渲染机制，输出一个包含JS代码的HTML文件，其核心思想还是借用了ECharts的底层库，
只是用Python封装了一次之后便于本地应用程序使用罢了。'''
# pyecharts创建图表,pyecharts的使用很简单，直接import需要用到的图表组件、设置相关参数、渲染即可。

# 1、生成柱状图
from pyecharts.charts import Bar
#导入bar类，bar类主要是用于柱状图的处理类

# bar = Bar()
# x_list=['数学', '语文', '英语', '历史', '地理', '化学']
# bar.add_xaxis(x_list)
# y_list=[95,80,76,84,75,90]
# bar.add_yaxis("张冰辉",y_list)
# bar.add_yaxis("小张",[91,8,56,64,95,50])
#
# bar.render("bar_test.html")
'''from pyecharts.charts import Bar 用于导入Bar 这个类，Bar就是用于柱状图处理的类。
bar = Bar() 实例化Bar类，命名为bar。
bar.add_xaxis()方法用于添加柱状图的X坐标数据，它可以接收一个列表或元祖数据。
bar.add_yaxis()方法用于添加柱状图的Y坐标数据，它可以接收一个列表或元祖数据。
bar.render()用于渲染结果HTML内容，不传参数默认文件名为 render.html，也可以自定义文件名作为参数传递进去。'''

#2、pyecharts的实际数据应用
from pyecharts.charts import Bar
bar=Bar()
bar.add_xaxis(['1978年','1980年','1990年','2000年','2017年','2018年'])
bar.add_yaxis("人均GDP",[449,565,2123,11471,98011,105399])
bar.add_yaxis("居民储蓄存款余额",[30,52,866,8240,84474,90273])
bar.render("gdp.html")
#饼状图
from pyecharts import options as opts
from pyecharts.charts import Pie
keys=['男性','女性']
values=[7322452,7438028]
data=zip(keys,values)
c=Pie()
c.add("饼状图",list(data))
c.set_global_opts(title_opts=opts.TitleOpts(title='男女比例情况'))
c.render('pie.html')

'''首先引入了一个新的库，叫做opts，该库主要用于图表参数设置的，
在这里我们用c.set_global_opts(title_opts=opts.TitleOpts(title="成都全市人口男女比例")) 
把图表标题设置为了成都全市人口男女比例，这个写法是pyecharts封装的不够优雅，
大家记住这种写法就是了，set_global_opts() 函数可以用来设置标题、工具条、提示文本等等。
在第6行有一个zip(keys,values)的操作，zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的列表。简单的说就是zip()函数可以用于重组多个迭代对象，
重组过程中相同元素下标的数据会被重新打包组合在一起，比如将["a","b","c"]和[1,2,3]这两个列表进行zip之后，
就会得到一个包含 三个元组('a', 1)、('b', 2)、('c', 3) 的对象，因为直接zip()之后得到的是一个迭代对象，
而不是列表或者元组数据，所以如果我们要直接将结果作为数据使用，需要进行一次类型转换 list(zip(**args))。
那么显而易见，本例子中的zip()结果就应该是 ('男性', 7322452)、('女性', 7438028)。这个数据正好是饼图需要的。
在第9行有一个 c.add("", list(data))的代码，Pie类的add()函数用于饼图绘制所需要用到的参数。
至于为什么第一个参数是一个空字符串，其实因为add()函数第一个参数名为series_name，用来表示序列名称，
其实在图表展示上没什么用处，所以我就给它设置为空字符串了，大家可以随意设置什么都行 。
最后list(data)没什么好说的，就是把zip结果转换成列表，
在11行的render()中，我自定义了输出文件名pie.html。'''





