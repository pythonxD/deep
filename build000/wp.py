import tensorflow as tf
import numpy as np
from matplotlib import style
#style.use('ggplot')

import matplotlib.pyplot as plt
import pandas as pd

def time_series(file):
    f = open(file,"r").read()
    if "," in f:
        f = f.replace(",",".")
        fc=open(file.replace(".","c."),"w")
        fc.write(f)
        fc.close()
        file = file.replace(".","c.")

    df = pd.read_csv(file, skiprows=1, sep=";")
    df = df.drop(["Bid", "Ask","Average price",  "Total volume", "Turnover",  "Trades",  "Unnamed: 11"],1)

    df = df.set_index("Date")
    df['20ma'] =  df['Closing price'].rolling(window=20,min_periods=0).mean()
    df['50ma'] =  df['Closing price'].rolling(window=50,min_periods=0).mean()
    df['100ma'] =  df['Closing price'].rolling(window=100,min_periods=0).mean()
    df['200ma'] =  df['Closing price'].rolling(window=200,min_periods=0).mean()
    df = df.sort_index(inplace=False)
    print(df)
    #df['50ma', '100ma', '200ma'].plot()
    #df['50ma','100ma'].plot()
##plot()!!!
    subp = plt.figure().add_subplot(111)
    #df['20ma'].plot(ax=subp,legend=True)
    #df['50ma'].plot(ax=subp,legend=True)
    #df['100ma'].plot(ax=subp,legend=True)
    #df['200ma'].plot(ax=subp,legend=True)

    subp.plot(df.index, df['20ma'])
    subp.plot(df.index, df['50ma'])
    subp.plot(df.index, df['200ma'])
    #df['Opening price'].plot(ax=subp,legend=True)
    #plt.scatter(df['50ma'], df['100ma'])
    plt.show()
    return df
time_series("data/OMXS30.csv")
