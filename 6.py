import os
import json
import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
gc_fake=[]
f = open('csv/gossipcop_fake_users.csv')
reader = csv.reader(f)
for col in reader:
    gc_fake.append(col[1])
fvalues,rvalues=[],[]
gc_real=[]
f = open('csv/gossipcop_real_users.csv')
reader = csv.reader(f)
for col in reader:
    gc_real.append(col[1])

for filename in os.listdir('user_followers'):
    with open(os.path.join('user_followers', filename), 'r') as f:
        jobj = json.loads(f.read())
        #print(jobj['followers'])
    with open(os.path.join('user_following', filename), 'r') as f:
        ass = json.loads(f.read())
        jobj['following']=ass['following']
        jobj['n_following'] = 0
        for follower in jobj['following']:
            #print(follower)
            if follower not in jobj['followers']:
                jobj['n_following']+=1
                #print(jobj['n_following'])
        jobj['n_followers'] = len(jobj['followers'])
        degreet = jobj['n_followers']+jobj['n_following']
    if str(filename[:-5]) in str(gc_fake):
        fvalues.append(degreet)
    if str(filename[:-5]) in str(gc_real):
        rvalues.append(degreet)
  
kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(fvalues, **kwargs, color='r', label='fake')
plt.hist(rvalues, **kwargs, color='g', label='real')
plt.gca().set(title='Degree distribution', ylabel='frequency')
plt.xlim(-100,10000)
plt.legend()
plt.show()
