import matplotlib
import pandas as pd
from  matplotlib import  pylab as plt
from  matplotlib import  font_manager


df =  pd.read_csv("lianjia_sz_clean.csv")
df.eval('ave_price = price / area',inplace=True)
df['ave_price'] = df['ave_price'].astype(int)
del df['Unnamed: 0']

df.to_csv("count_data_add.csv")


# plt.savefig("./img/price_number_under2000.png")
# plt.show()



