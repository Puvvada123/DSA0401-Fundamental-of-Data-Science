import numpy as np
import pandas as pd
a=pd.read_csv("D:\execl\lkiou.csv")
print(a)
avg=np.mean(a,axis=0)
print(avg)
h=np.argmax(avg)
sub=['english','maths','science','history']
print(sub[h],'=',max(avg))
