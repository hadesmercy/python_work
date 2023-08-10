import matplotlib
import pandas as pd
import  seaborn as sns
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

df =  pd.read_csv("count_data_add.csv")
#print(df['location2'].value_counts())
#print(df['price'].groupby(df['location2']).mean())

t  = df['price'].groupby(df['location2']).mean()
tt = t.to_frame()

tt.to_csv("final.csv")

new = pd.read_csv('final.csv')
new['price'] = new['price'].astype(int)
new = new.sort_values(by='price',ascending=False)
print(new)
# tt['location2'] = tt['location2'].astype('str')
plt.figure(figsize = (8,24),dpi=300)
plt.yticks(fontsize = 8)
out = sns.barplot(x = 'price',y ='location2' ,data=new)
plt.xlabel("每月租金/元")
plt.ylabel("板块名称")
for i in out.containers:
    out.bar_label(i,)


# plt.show()


plt.savefig("price_location.png")
plt.show()