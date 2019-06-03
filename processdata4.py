#coding = utf-8
#标准化计算公式(正态分布)
#(数值 -  平均值 )/ 标准差
#标准差 = 根号下(数值 - 平均值)² / N
import numpy as np
data =np.array([
    [1,2],
    [3,4],
    [5,6]
])

mean = (np.mean(data[:,1]))
std = np.std(data[:,1])

print((data[:,1] -mean) / std)