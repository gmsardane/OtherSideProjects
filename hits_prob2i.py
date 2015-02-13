
'''
I.
Highest probability of a transition to a different category. 
Give a tuple 'Category1, Category2, probability'

Usage: ipython hits_prob2i.py 

'''
import pandas as pd
df = pd.read_csv("hits.csv") #import data
dfx = df.sort_index(by=['user', 'time'], ascending=[True, True]) #sort data by user then time

dd = dfx#[0:20] #test only a fraction of the data

dd["ndx"] = dd.index #make a new column and populate it by the index
dd['ndx2'] = dd['ndx'].shift(1) #make another column and populate it by shifted index

#x = initial, y = final 
fin = pd.merge(dd, dd, how = 'left', left_on = 'ndx', right_on = 'ndx2') #left join dd to dd on ndx = ndx2
fin["user"]=fin["user_x"]-fin["user_y"] #make a new column, "user", which is the difference of user
fix = fin[fin["user"]==0] #make sure that "user" = 0, meaning the "user" is the same for the transition

a = fix.groupby(['category_x','category_y'], as_index=False).user.count() #count (i,j) transitions
b = fix.groupby(['category_x'], as_index=False).time_x.count() #count i's

c = pd.merge(a, b, how = 'left', left_on = 'category_x', right_on = 'category_x') #left join a to b on ndx = ndx2

c["prob"]=c["user"]/c["time_x"]

print c.sort_index(by=['prob'], ascending=[False])

