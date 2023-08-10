
import pandas
from pandas.io.json import json_normalize
import pandas as pd
import json


def paring(infile_name,outfile_name):
    with open(infile_name, 'r', encoding="utf-8") as f:
        res = f.readlines()
    data = []
    for key_ in res:
        # print(key_)
        json_data = json.loads(key_)
        #print(json_data)
        data.append(json_data)
        #print(data)
    # print(data)
    df = pandas.json_normalize(data)
    df.to_csv(outfile_name)
    print('done')


if __name__ == '__main__':
    paring('lianjia.json','lianjia_sz.csv')