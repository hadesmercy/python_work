#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

import pandas as pd
import numpy as np


df = pd.read_csv("lianjia_sz.csv",low_memory=False)
print(len(df))
df = df.dropna()



print(len(df))


df.drop_duplicates(subset=['url'], keep='first', inplace=True)


print(len(df))
df['area'] = df['area'].apply(lambda x: x[0:-1])
df['area'] = df['area'].astype(float)
df['price'] = df['price'].astype(float)

df['area'] = df['area'].astype(int)
df['price'] = df['price'].astype(int)
df.to_csv("lianjia_sz_clean.csv")

#用来去除面积后所携带的单位


if __name__ == '__main__':
    pass

