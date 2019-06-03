#抽取一个函数
import numpy as np
import collections as c
def knn(k,predictPoint,feature,label):
    # 计算每个投掷点距离predictPoint的距离
    distance = list(map(lambda x: abs(predictPoint - x), feature))
    # 对distance的集合元素从小到大排序(返回的排序的下标位置)
    sortindex = (np.argsort(distance))
    # 用排序的sortindex来操作label集合
    sortlabel = label[sortindex]
    # .most_common取最常见的数出现的次数
    return (c.Counter(sortlabel[0:k]).most_common(1)[0][0])

if __name__ == '__main__':
    traindata = np.loadtxt("data_train.csv",delimiter=",")
    #输入值
    feature = traindata[:, 0]
    #结果
    label = traindata[:, -1]
    #预测点,来自测试数据的每一条记录
    testdata = np.loadtxt("data_test.csv",delimiter=",")
    #k的取值一般为总数目开平方
    # for k in range(1,100):
    #     count = 0
    #     for item in testdata:
    #         prodict = knn(k,item[0],feature,label)
    #         real = item[1]
    #         if prodict == real:
    #             count = count + 1
    #     print("k = {},准确率:{}".format(k,count*100.0/len(testdata)))
    print(knn(36,200,feature,label))