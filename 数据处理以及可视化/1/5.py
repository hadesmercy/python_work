import matplotlib
import pandas as pd
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

df =  pd.read_csv("小于一部分的数字.csv")
del df['Unnamed: 0']
del df['Unnamed: 0.1']
del df['Unnamed: 0.1.1']
print(df.describe())
