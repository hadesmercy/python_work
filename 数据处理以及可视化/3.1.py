
import pandas as pd
import  seaborn as sns
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

df =  pd.read_csv("count_data_add.csv")
plt.figure(figsize = (40,8),dpi=300)
plt.scatter(df['orientation'],df['ave_price'])
plt.xlabel('朝向')
plt.ylabel('平均价格（元/月）')
plt.title('朝向与价格的关系')
plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.savefig('朝向与价格的关系')
plt.show()

