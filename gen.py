import pandas as pd
import random
import numpy as np

wordnum = 20
lenrange = 7

alph_e = pd.read_table('time_e_a.txt')
comb_e = pd.read_table('time_e_c.txt').values
index_e=alph_e.sort_values('times',ascending=False)[:lenrange].index.tolist()
alist_e = [i[0] for i in alph_e.values]
#print(index_e)

val = [i[1] for i in comb_e]
n=int(np.sqrt(len(val)))
new=pd.DataFrame(np.array(val).reshape(n,n).tolist())
df1 = new.iloc[index_e, index_e]
combtimes_e = np.array(df1, dtype='int64')
rsum = combtimes_e.sum(axis=1)
ptable_e=combtimes_e/rsum[:, np.newaxis]
with open('pandas.txt', mode='w') as f:

    f.write(pd.DataFrame (ptable_e,columns=['e', 'o', 't','h', 'a', 'i', 's']).to_string(header = True, index = True))
print()

print(", ".join([alist_e[i] for i in index_e]))
for __ in range(wordnum):
    word=[random.randint(0,lenrange-1)]
    for _ in range(random.randint(2,10)):
        w = word[-1]
        word.extend(random.choices(list(range(lenrange)), weights=ptable_e[w], k=1))
    print("".join([alist_e[index_e[i]] for i in word]))


alph_g = pd.read_table('time_a.txt')
comb_g = pd.read_table('time_c.txt').values
index_g=alph_g.sort_values('times',ascending=False)[:lenrange].index.tolist()
alist_g = [i[0] for i in alph_g.values]
#print(index_g)

val = [i[1] for i in comb_g]
n=int(np.sqrt(len(val)))
new=pd.DataFrame(np.array(val).reshape(n,n).tolist())
df1 = new.iloc[index_g, index_g]
combtimes_g = np.array(df1, dtype='int64')
rsum = combtimes_g.sum(axis=1)
ptable_g=combtimes_g/rsum[:, np.newaxis]

print(", ".join([alist_g[i] for i in index_g]))
for __ in range(wordnum):
    word=[random.randint(0,lenrange-1)]
    for _ in range(random.randint(2,10)):
        w = word[-1]
        word.extend(random.choices(list(range(lenrange)), weights=ptable_g[w], k=1))
    print("".join([alist_g[index_g[i]] for i in word]))

alph_t = pd.read_table('time_t_a.txt')
comb_t = pd.read_table('time_t_c.txt').values
index_t=alph_t.sort_values('times',ascending=False)[:lenrange].index.tolist()
alist_t = [i[0] for i in alph_t.values]
#print(index_t)

val = [i[1] for i in comb_t]
n=int(np.sqrt(len(val)))
new=pd.DataFrame(np.array(val).reshape(n,n).tolist())
df1 = new.iloc[index_t, index_t]
combtimes_t = np.array(df1, dtype='int64')
rsum = combtimes_t.sum(axis=1)
ptable_t=combtimes_t/rsum[:, np.newaxis]

print(", ".join([alist_t[i] for i in index_t]))
for __ in range(wordnum):
    word=[random.randint(0,lenrange-1)]
    for _ in range(random.randint(2,10)):
        w = word[-1]
        word.extend(random.choices(list(range(lenrange)), weights=ptable_t[w], k=1))
    
    print("".join([alist_t[index_t[i]] for i in word]))
