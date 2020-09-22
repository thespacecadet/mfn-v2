# collect data from a csv

import pandas as pd 
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
datapath = os.path.join(dir_path, "data.csv")
dataopen = open(datapath)
# s = open("data.csv")
datapd = pd.read_csv(datapath)
print(datapd.head)