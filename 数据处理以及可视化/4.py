import matplotlib
import pandas as pd
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

df =  pd.read_csv("count_data_add.csv")
plt.figure(dpi=1000)
plt.xlabel("每月租金/元")
plt.ylabel('数量/个')

df['price'].hist()
plt.savefig("price_number_all.png")
plt.show()



under = df[df['price'] < 200000]
under.to_csv('小于一部分的数字.csv')
df['price'].value_counts().to_csv('计算众数.csv')


under['price'].hist()
plt.xlabel("每月租金/元")
plt.ylabel('数量/个')
plt.savefig("price_number_under1.png")
plt.show()

under = df[df['price'] < 20000]
under['price'].hist()
plt.xlabel("每月租金/元")
plt.ylabel('数量/个')
plt.savefig("price_number_under2.png")
plt.show()

