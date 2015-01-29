import pickle
from ggplot import *
file = open("score_dfs.pickle",'rb')
dfs = pickle.load(file)

for i in range(0, len(dfs)):
    dfs[i].to_csv("data/scores" + str(i) + ".csv", encoding='utf-8')