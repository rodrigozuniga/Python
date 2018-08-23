import pandas as pd, numpy as np,os
import matplotlib.pyplot as plt,  seaborn as sns
from sklearn import datasets
# Set default Seaborn style
sns.set()
iris = datasets.load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

d={0.0:"Setosa",1.0:"Versicolor",2.0:"Virginica"}
df['target']=df.target.map(d)
sns.swarmplot(x='target',y='petal length (cm)',data=df)

plt.title('Iris Petal Length Swarmplot')
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.grid('True')
os.chdir("C:\\Users\\rodri\\Python")
print(os.getcwd())
plt.show()
plt.savefig("swarmplot_iris.pdf", transparent = True)


# """Exploratory data analysis can never be the
# whole story, but nothing else can serve as
# the foundation stone.  --John Tukey"""
