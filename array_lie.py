import numpy as np
import pandas as pd 
import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np 
from sklearn.cluster import KMeans
import math
df = pd.read_excel('BIM3010_Fall_2019_Homework4th.xls')
data = np.array(df.values)
print(data)

sample = ['GSM101095','GSM101096',	'GSM101097', 'GSM101098',	'GSM101099',	'GSM101100',	'GSM101101',	'GSM101102',	'GSM101103',	'GSM101104',	'GSM101105',	'GSM101106',	'GSM101107',	'GSM101108',	'GSM101109',	'GSM101110',	'GSM101111',	'GSM101112',	'GSM101113',	'GSM101114',	'GSM101115',	'GSM101116']
normal_data = {'Gene Label':data[:,2]}


for sam in range(3,25):
    normal = sum(data[:,sam])/len(data[:,sam])
    norm = np.array(data[:,sam]/normal)
    normal_data[sample[sam-3]]=np.log2(norm.astype('float64'))

df = pd.DataFrame(normal_data, index=data[:,0])
df.to_excel(r'log_2trans.xlsx')
