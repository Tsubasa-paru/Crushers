# -*- coding: utf-8 -*-
#[6_Name, 7_Select one, 8_Weight, 9_Rep]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import math

args = sys.argv
df = pd.read_csv(args[1]) 
file_name = args[1]
file_name = file_name[:-4]
#print(file_name)

df = df.rename(columns={'6_Name':'Name', 'feedback_date':'Date', '7_Select one':'Event', '8_Weight':'Weight', '9_Rep':'Rep'})
df = df.loc[:, ["Name","Date","Event","Weight","Rep"]]
df["Date"] = df["Date"].str.replace("(.*)T(.*)", r"\1")
#print(df)

players = df["Name"].unique()
events = df["Event"].unique()

print(players)
for name in players:
    player = df[df["Name"].isin([name])]
    player = player.sort_values("Date")
    print(player)

    player.to_csv(name+file_name+".csv",columns=["Date","Event", "Weight", "Rep"],index=False)
    #for event in events:
      
    '''
    fig = plt.figure()
    plt.grid()
    plt.title(name+"_BenchPress") 
    plt.xlabel(file_name[-6:])
    plt.ylabel("Score")
    plt.xticks(np.arange(0, 31 + 1, 1))
    plt.yticks(np.arange(int(min(bench_list)/10)*10,int(max(bench_list)/10)*11,10))
    plt.plot(date_list, bench_list)
    plt.show()

    fig.savefig(file_name+"_bench.png")
    result = file_name[:-4]+"result"
    df.to_csv(result+".csv",columns=["date","BenchPress"],index=False)
    '''