#https://www.cnblogs.com/liulinghua90/p/9935642.html

#https://blog.csdn.net/liuyq859/article/details/78387600
import pandas as pd 
import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np 
from sklearn.cluster import KMeans
df = pd.read_excel('BIM3010_Fall_2019_Homework4th.xls')
data = np.array(df.values)
#data=format(data)
nonSaverage = [] # record average number of gene expression level for non-smoker
Saverage = [] # average gene expression level for smoker
FC = [] #record fold change of each gene
Pvalue=[]
logadjPvalue = [] #record statistical significance of gene expression difference between smoker and non-smoker
DEG = [] #record differencial expression genes
for i in range(len(data)):
    nonSaverage.append(sum(data[i][3:15])/12)
    Saverage.append(sum(data[i][15:25])/10)
    fc = math.log2((sum(data[i][15:25])/10)/(sum(data[i][3:15])/12))
    FC.append(fc) #calculate fold change of each gene
    #P = stats.ttest_ind(data[i][3:15],data[i][15:25],equal_var=False).pvalue
    P = stats.ttest_ind(data[i][3:15],data[i][15:25],equal_var=False).pvalue
    Pvalue.append(P)
rankp= sorted(Pvalue)



f = 'DEG.txt'
fil=open(f,'w')
f2 = 'DEGLabel.txt'
fil2=open(f2,'w')
f3 = 'detail.txt'
fil3 = open(f3,'w+')
fil3.write(str(np.matrix(['ID','log2FC','Pvalue', '-log10adjPvalue'])))
f4 = 'DEGinfor.txt'
fil4 = open(f4,'w+')
DEGdata = []
for i in range(len(data)):
    adjP = Pvalue[i]*len(data)/(rankp.index(Pvalue[i])+1)
    logadjPvalue.append(-math.log10(adjP))
    

    if abs(FC[i]) >= 1 and adjP < 0.05:
        DEGdata.append(data[i][3:25])
        DEG.append(data[i][0])
        fil.write(data[i][0])
        fil.write('\n')
        fil2.write(data[i][2])
        fil2.write('\n')
    detail = np.matrix([data[i][0], FC[i], Pvalue[i], logadjPvalue[i]])
    fil3.write(str(detail))
    fil3.write('\n')
    fil4.write(data[i][0]+''+str(data[i][3:25]))
    fil4.write('\n')
print(DEGdata)

# clustering
DEG = np.array(DEGdata)
kmeans = KMeans(n_clusters = 3, random_state=0).fit(DEG)
print(kmeans.labels_)


        
fil.close()
fil2.close()
fil3.close()
fil4.close()
#print(FC)
#print(logadjPvalue)
#len(data)*
x1=[-1,-1]
y1=[0,3]
x2=[1,1]
y2=[0,3]
x3=[-3,6]
y3=[-math.log10(0.05),-math.log10(0.05)]
plt.plot(x1,y1,x2,y2,x3,y3,color='black',linestyle='--')
print(len(FC))
plt.scatter(FC,logadjPvalue,s=2)
plt.show()




    


