
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF


samples_std1=np.random.normal(20,1,size=100000)
samples_std3=np.random.normal(20,3,size=100000)
samples_std10=np.random.normal(20,10,size=100000)

ecdf1=ECDF(samples_std1)
ecdf3=ECDF(samples_std3)
ecdf10=ECDF(samples_std10)
x_std1,y_std1=ecdf1.x,ecdf1.y
x_std3,y_std3=ecdf3.x,ecdf3.y
x_std10,y_std10=ecdf10.x,ecdf10.y
plt.plot(x_std1,y_std1,marker='.',linestyle='none')
plt.plot(x_std3,y_std3,marker='.',linestyle='none')
plt.plot(x_std10,y_std10,marker='.',linestyle='none')
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.grid()
plt.show()
