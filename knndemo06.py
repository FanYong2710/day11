#coding = utf-8
#向量是欧式距离和标准化的结合
import numpy as np
feature = np.array([
    [-121,47,33],
    [-121.2,46.5,333],
    [-122,46.3,32],
    [-122.9,46.7,323],
    [-120.1,46.2,32]
])
label = np.array([
    200,210,250,215,232
])
predictPoint = np.array([-121,46,323])
matrixtemp = (feature - predictPoint)
matrixtemp2 = np.square(matrixtemp)
#axis = 1 代表逐行想加
sortindex = np.argsort(np.sqrt(np.sum(matrixtemp2,axis=1)))
sortlabel = label[sortindex]
k = 3
#数据标准化
predictprice = np.sum(sortlabel[0:k])/k
print("预测的房价是{}万".format(predictprice))