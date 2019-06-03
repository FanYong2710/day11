#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-5-15
'''
import  numpy as np
import collections as c

# sortedlabel = np.array([2,2,2,3,3,1])
# #什么元素出现几次(label,结果)
# print(c.Counter(sortedlabel))
# #列表-元组-元素
# print(c.Counter(sortedlabel).most_common(1)[0])
# #几种数字出现了几次,根据索引取值
# print(c.Counter(sortedlabel).most_common(2)[0][0])

data = np.loadtxt("data0.csv",delimiter=",")
print(data)
