import pandas as pd, numpy as np, matplotlib.pyplot as plt
import plotly.plotly as py
exec(open("C:\Pw\plotly_pw.txt").read())
from sklearn import datasets
iris = datasets.load_iris(return_X_y=False)
iris.target_names
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['target']=iris.target
df['target_name']=iris.target_names[iris.target]
mn_slength=df.groupby('target_name').mean()['sepal length (cm)']
plt.figure(1,figsize=(8, 8))
plt.bar(mn_slength.index,mn_slength.values,color='red')
plt.title('Average Sepal Length by Iris Type')
plt.xlabel('Iris Type')
plt.ylabel('Average Sepal Length')
plt.grid(True)
plt.figure(2,figsize=(8, 8))
plt.barh(mn_slength.index,mn_slength.values,color='blue')
plt.title('Average Sepal Length by Iris Type')
plt.xlabel('Average Sepal Length')
plt.ylabel('Iris Type')
plt.grid(True)
plt.figure(1,figsize=(8, 8))
mns=df.groupby('target_name').mean()[['sepal length (cm)','sepal width (cm)']]
mns.columns=['Avg.Length','Avg.Width']
mns.index.name='Iris Type'
bar_avg=mns.plot.bar(figsize=(10,8),grid=True,title='Avg Length and Width by Iris Type',rot=0,fontsize=14)
plt.ylabel('cm',fontsize=14)
plt.xlabel('Iris Type',fontsize=12)
