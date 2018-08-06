import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets as ds

dt=np.random.randn(500)
gr=np.random.randint(0,3,500)
L=['A','B','C']
gr2=[L[i] for i in gr]

#Pandas:
df=pd.DataFrame({'Value':dt,'Group':gr2})
bx=df.boxplot(by='Group')
bx.figure.suptitle('')
plt.title('Distribution by Group')
#Plt:
plt.figure()
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)
print(type(collectn_1))
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
plt.boxplot(data_to_plot)
plt.title('Distribution by Group')
plt.xticks([1, 2, 3, 4], ['A', 'B', 'C','D'])
plt.grid(True)


# ?plt.boxplot
