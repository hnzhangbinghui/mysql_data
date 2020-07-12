from pyecharts import options as opts
from pyecharts.charts import Bar,Grid,Line,Liquid,Page,Pie

def pie_echart():
    keys = ['男性', '女性']
    values = [7322452, 7438028]
    data = zip(keys, values)
    c = Pie()
    c.add("饼状图", list(data))
    c.set_global_opts(title_opts=opts.TitleOpts(title='男女比例情况'))
    return c
def bar_echart():
    c = Bar()
    c.add_xaxis(['1978年', '1980年', '1990年', '2000年', '2017年', '2018年'])
    c.add_yaxis("人均GDP", [449, 565, 2123, 11471, 98011, 105399])
    c.add_yaxis("居民储蓄存款余额", [30, 52, 866, 8240, 84474, 90273])
    return c

if __name__=='__main__':
    page=Page()
    page.add(pie_echart(),bar_echart(),pie_echart(),bar_echart())
    page.render("all.html")