#抽取一个函数
import numpy as np
import collections as c
#一维数组
def knn(k,predictPoint,feature,label):
    # 计算每个投掷点距离predictPoint的距离
    distance = list(map(lambda x: abs(predictPoint - x), feature))
    # 对distance的集合元素从小到大排序(返回的排序的下标位置)
    sortindex = (np.argsort(distance))
    # 用排序的sortindex来操作label集合
    sortlabel = label[sortindex]
    # .most_common取最常见的数出现的次数
    return (c.Counter(sortlabel[0:k]).most_common(1)[0][0])

#二维数组
#欧式距离
def knn2(k,predictPoint,ballcolor,feature,label):
    #计算每个投掷点到(PredictPoint,ballcolor)的距离
    distance = list(map(lambda item : ((item[0]-predictPoint)**2+(item[1]-ballcolor)**2)**0.5,feature))
    # 对distance的集合元素从小到大排序(返回的排序的下标位置)
    sortindex = (np.argsort(distance))
    # 用排序的sortindex来操作label集合
    sortlabel = label[sortindex]
    # .most_common取最常见的数出现的次数
    return (c.Counter(sortlabel[0:k]).most_common(1)[0][0])

def knn3(k,predictPoint,ballcolor,feature,label):
    #计算每个投掷点到(PredictPoint,ballcolor)的距离
    distance = list(map(lambda item : ((item[0]/475-predictPoint/475)**2+((item[1]-0.50)/0.05-(ballcolor-0.50)/0.05)**2)**0.5,feature))
    # 对distance的集合元素从小到大排序(返回的排序的下标位置)
    sortindex = (np.argsort(distance))
    # 用排序的sortindex来操作label集合
    sortlabel = label[sortindex]
    # .most_common取最常见的数出现的次数
    return (c.Counter(sortlabel[0:k]).most_common(1)[0][0])
if __name__ == '__main__':
    traindata = np.loadtxt("data2-train.csv",delimiter=",")
    #输入值
    feature = traindata[:, 0:2]
    #结果
    label = traindata[:, -1]
    #预测点,来自测试数据的每一条记录
    testdata = np.loadtxt("data2-test.csv",delimiter=",")
    #k的取值一般为总数目开平方
    k = 36
    count = 0
    for item in testdata:
        predict = knn3(k,item[0],item[1],feature,label)
        real = item[-1]
        if predict == real:
            count += 1

    print("准确率:{}%".format(count*100.0/len(testdata)))