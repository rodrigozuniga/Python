import pandas as pd, numpy as np
import datetime as dt
import calendar as cl
import matplotlib.pyplot as plt
import matplotlib as mpl
dt1=dt.date(2019,1,1)
dt2=dt1+dt.timedelta(days=1)
dt1.strftime('%Y/%m/%d')
rnd=np.random.randn(25)
rnd2=np.random.randn(25)
days=[int(d) for d in np.arange(0,25)]
dts=[dt1+dt.timedelta(days=days[d]) for d in days]
dts2=[x.strftime('%m/%d') for x in dts]
dts2
L=list(zip(dts2,rnd,rnd2))
df=pd.DataFrame(L,columns=['Date','Value1','Value2'])
plt.figure(1,figsize=(10,10))
# plt.subplot(221)
f1,sb1=plt.subplots(1,figsize=(9,9))
sb1.hlines(0,0,24,color='red',lw=4)
# mpl.axes.Axes.axhline(y=0,xmin=0,xmax=1,linewidth=4, color='r')
plt.scatter(df['Date'],df['Value1'])
plt.plot(df['Date'],df['Value1'])
plt.scatter(df['Date'],df['Value2'])
plt.plot(df['Date'],df['Value2'])
plt.xticks(rotation='vertical')
plt.grid(True)
plt.title('Normally Distributed Variables',color='blue')
plt.legend(('Value1','Value2'))
plt.ylabel('Value')
plt.xlabel('Date')
#df.plot() for graphing time series
plt.figure(figsize=(15,15))
df['dts']=dts
gr=df.set_index('dts').plot(lw=3,style=['-', '--'],marker='o',figsize=(9,9))
#add horizontal line
gr.axhline(0,0,10,color='red',lw=4)
plt.xticks(rotation='vertical')
plt.grid(True)
plt.title('Normally Distributed Variables',color='blue')
plt.ylabel('Value')
plt.xlabel('Date')
