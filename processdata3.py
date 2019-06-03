#coding = utf-8
#归一化公式
# (X - Xmin) / (Xmax - Xmin)
import numpy as np
data =np.array([23,12,35,111,36,44,66,74])

print((data - np.min(data)) / (np.max(data) - np.min(data)))