import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = [20, 10] # for square canvas
#完成"C0N0","C0N3","C0N7","C0N8","C0N9","C1C1","C1N0","C1N1","C1N3","C1N7","C1N8","C1N9"
#出问题"C0C1",

#


# xticks = list(range(257, 364, 3))
# xticks2 = list(range(257, 364, 3))
# print(xticks)
# for i in xticks2:
#     xticks.append(i)
# print(xticks)
#"C0C0","C0C1","C1C1",
#"C0N0","C0N1","C0N3","C0N7","C0N8","C0N9","C1N0","C1N1","C1N3","C1N7","C1N8","C1N9"
for file in ["C0C0","C0C1","C1C1"]:
    print(file)
    grid = plt.GridSpec(2, 2, wspace=0.1, hspace=0.3,left = 0.05,right=0.95)

    l1 = plt.subplot(grid[0, 0])
    l2 = plt.subplot(grid[0, 1:])
    l3 = plt.subplot(grid[1, 0])
    l4 = plt.subplot(grid[1, 1:])
    
    for chain in ["A","B"]:
        csv_file = file+"_"+chain+"_data_"+"prob.csv"
        csv_data = pd.read_csv(csv_file, header = None)#防止弹出警告
        csv_df = pd.DataFrame(csv_data)

        #plt.title("interaction for "+ file+"_chain_"+ chain)
        x = csv_df[0]
        y = csv_df[1]

        csv_file_t = file+"_"+chain+"_data_"+"prob_total.csv"
        csv_data_t = pd.read_csv(csv_file_t, header = None)#防止弹出警告
        csv_df_t = pd.DataFrame(csv_data_t)


        x_t = csv_df_t[0]
        y_t = csv_df_t[1]

        maxy = max(max(list(y)),max(list(y_t)))

        if file[2] == 'N':
            if chain == 'A':
                num_p = 43
            else:
                num_p = 256
        if file[2] == 'C':
            num_p = 256
       
        
        index1 = list(x).index(108) + 1
        index2 = list(x_t).index(108)+1
        if chain == "A":
            l11 = l1.plot(x[0:index1]+num_p,y[0:index1]*100,color= "red",label='Selective')
            l12 = l1.plot(x_t[0:index2]+num_p,y_t[0:index2]*100,color= "black",label = 'All' )
            l21 = l2.plot(x[index1:]+146,y[index1:]*100,color= "red",label='Selective')
            l22 = l2.plot(x_t[index2:]+146,y_t[index2:]*100,color= "black",label = 'All')
            l1.legend(loc = "upper left")
            l2.legend(loc = "upper left")
            l1.grid(axis = "x")
            l1.grid(axis = "y")
            l2.grid(axis = "x")
            l2.grid(axis = "y")
            l1.set_xlabel("Residue ID")
            l1.set_ylabel("Probability (%)")
            l2.set_xlabel("Residue ID")
            l2.set_ylabel("Probability (%)")
            title = file[0:2] 
            l1.title.set_text("CTD "+title+" monomer 1")
            l2.title.set_text("CTD "+title+" monomer 2") 
            l1.set_ylim([-1,45])
            l2.set_ylim([-1,45])
        if chain == "B":
            l31 = l3.plot(x[0:index1]+num_p,y[0:index1]*100,color= "red",label='Selective')
            l32 = l3.plot(x_t[0:index2]+num_p,y_t[0:index2]*100,color= "black",label = 'All' )
            l41 = l4.plot(x[index1:]+146,y[index1:]*100,color= "red",label='Selective')
            l42 = l4.plot(x_t[index2:]+146,y_t[index2:]*100,color= "black",label = 'All')
            l3.legend(loc = "upper left")
            l4.legend(loc = "upper left")
            l3.grid(axis = "x")
            l3.grid(axis = "y")
            l4.grid(axis = "x")
            l4.grid(axis = "y")
            l3.set_xlabel("Residue ID")
            l3.set_ylabel("Probability (%)")
            l4.set_xlabel("Residue ID")
            l4.set_ylabel("Probability (%)")
            title = file[2:] 
            l3.title.set_text("CTD "+title+" dimer 1")
            l4.title.set_text("CTD "+title+" dimer 2") 
            l3.set_ylim([-1,45])
            l4.set_ylim([-1,45])       
        
        #l1.set_xticks(range(257, 364, 3)) 
        #l2.set_xticks(range(257, 364, 3)) 

            # l3.grid(axis="y")
            # l3.grid(axis = "x")
            # l31 = l3.plot(x+num_p,y*100,color= "red",label='Selective')
            # l32 = l3.plot(x_t+num_p,y_t*100,color= "black",label = 'All' )
            # l3.legend(loc = 'upper left')
            # l3.set_xlabel("Residue ID")
            # l3.set_ylabel("Probability (%)")
            # l3.title.set_text("NTD")  
            # l3.set_ylim([-1,50])  

        
    plt.suptitle("Interaction for "+ file)

    plt.savefig(file+'_plot.png')
    plt.show()#show()在保存之前会导致保存一片空白
        
        #plt.pause(2)
#            plt.close()