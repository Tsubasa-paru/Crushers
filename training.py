# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import math
#import csv

args = sys.argv
#csvfile = open("w-training.csv")
df = pd.read_csv(args[1]) #, usecols=["bp_s", "bp_n","sq_s","sq_n"])

file_name = args[1]
file_name = file_name[:-4]

bench_list = []
squat_list = []
date_list = []

repeat = len(df)
for n in range(0, repeat, 10):
    day = df.iloc[n:n+8,]
    date_list.append(df.loc[n,"date"])
    #print(n)
    #print(day)
    bench_press = day["BenchPress"].str.split("-")
    #print(bench_press)
    b_eval = 0
    for i in range(len(bench_press)+n):
        try:
            b_set = bench_press[i]
            weight = float(b_set[0])
            num = float(b_set[1])
            b_eval += math.exp(weight / 30) * math.log(num)
            #print("tmp_eval:",int(eval))
        except:
            None
            #print("Key Error_B",n,i)
            
    print("bench_eval:", int(b_eval))
    bench_list.append(b_eval)

    squat = day["Squat"].str.split("-")
    #print(squat)
    s_eval = 0
    for j in range(len(squat)+n):
        try:
            s_set = squat[j]
            weight = float(s_set[0])
            num = float(s_set[1])
            s_eval += math.exp(weight / 30) * math.log(num)
            #print("tmp_eval:",int(eval))
        except:
            None
            #print("Key Error_S",n,j)
        
    print("squat_eval:", int(s_eval))
    squat_list.append(s_eval)

print(date_list)

player = file_name.split("_")
player = player[0]

fig = plt.figure()
plt.grid()
plt.title(player+"_BenchPress") 
plt.xlabel(file_name[-6:])
plt.ylabel("Score")
plt.xticks(np.arange(0, 31 + 1, 1))
plt.yticks(np.arange(int(min(bench_list)/10)*10,int(max(bench_list)/10)*11,10))
plt.plot(date_list, bench_list)
plt.show()

fig.savefig(file_name+"_bench.png")
#result = file_name[:-4]+"result"
#df.to_csv(result+".csv",columns=["date","BenchPress"],index=False)