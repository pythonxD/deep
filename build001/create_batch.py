import pandas as pd
import matplotlib.pyplot as plt

dfm = pd.read_csv("data/OMXS30c.csv", sep=";", skiprows=1)

df = dfm['Closing price'] #get data from csv

df['new'] = df.iloc[::-1].values #get a list with values (closing prices)

data = pd.DataFrame({'p':df['new']}) #create a df with time series
print(data)
#print(df['new'])
#data.plot()
#plt.show()

# creating batches
batch_size = 100
size = len(data)

amount_batches = round((size / batch_size)-0.49) # round modified to round down

print(size)
print(amount_batches)
all_batches =[]




for i in range(amount_batches):
    #batchi = data[size-batch_size*(i+1):size-batch_size*i].values.tolist()#reverse
    batchi = data[i*batch_size:(i+1)*batch_size].values.tolist()
    all_batches.append(batchi)


print(len(all_batches))
#print(all_batches) #debug all batches
for i in range(len(all_batches)):
#for i in range(round(len(all_batches)/(len(all_batches)*0.015))):
    #fig = plt.figure(figsize=(16, 9))
    plt.plot(range(len(all_batches[i])),all_batches[i], label="#"+str(i))
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=20, mode="expand", borderaxespad=0.)
    #plt.legend(loc='upper left')
    #plt.xlabel('batch_index', fontsize=18)
    #plt.ylabel('$', fontsize=16)
    #plt.legend(title = "allbatch"+str(i))
plt.show()
