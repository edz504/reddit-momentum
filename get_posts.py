import praw
import numpy as np 
import pandas as pd
import datetime, time, sys, pickle
from ggplot import *

user_agent = "post-momentum-tracker"
r = praw.Reddit(user_agent=user_agent)
NUM_POSTS = 10 # number of posts
FREQ = 20 # frequency of updated scores (in seconds)
END = 12 # number of hours to continue updating
LENGTH = END * 60 * (60 / FREQ) # length of array needed to store
index = range(0, LENGTH)

submissions = r.get_subreddit('funny').get_rising(limit=NUM_POSTS)
s_list = [x for x in submissions]
ids = [x.id for x in s_list]

dfs = []
columns = ['time', 'score', 'ups', 'downs']
# make a dataframe for each post
for i in ids:
    dfs.append(pd.DataFrame(index=index, columns=columns))

for t in index:
    for post_i in range(0, NUM_POSTS):
        this_time = datetime.datetime.now()
        post_update = r.get_submission(submission_id=ids[post_i])
        this_df = dfs[post_i]
        this_df.loc[t] = [this_time,
            post_update.score,
            post_update.ups,
            post_update.downs]
        sys.stdout.write('.')
    print
    time.sleep(FREQ)

with open('score_dfs.pickle', 'wb') as handle:
  pickle.dump(dfs, handle)

# plotting
p = ggplot(aes(x='time', y='score'), data=dfs[0]) + geom_point()