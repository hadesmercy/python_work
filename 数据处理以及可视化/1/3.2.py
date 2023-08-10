
import pandas as pd
import  seaborn as sns
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
df =  pd.read_csv("count_data_add.csv")
plt.figure(dpi=300)
plt.scatter(df['area'],df['price'])
plt.xlabel('面积（平方）')
plt.ylabel('价格（元/月）')
plt.grid(linestyle=":", color="r")
plt.title('价格与面积的关系')
plt.savefig('价格与面积的关系')
plt.show()

