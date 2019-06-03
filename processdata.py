#coding = utf-8
'''
    标题训练数据与测试数据
    @name:测试数据是训练数据的1/10:测试数据test100   训练数据train1000
    @function:求k值
    @author: Mr.Fan
    @date:2019-5-15
'''
import numpy as np

data = np.loadtxt("data0.csv",delimiter=",")
#打散数据
np.random.shuffle(data)
print(data)

#测试集数据100
test_data = data[0:100]
#训练集数据1000
train_data = data[100:-1]
#保存测试数据 %d以整型的方式保存
np.savetxt("data_test.csv",test_data,delimiter=",",fmt="%d")
#保存训练数据  训练数据的量是测试数据的十倍
np.savetxt("data_train.csv",train_data,delimiter=",",fmt="%d")
