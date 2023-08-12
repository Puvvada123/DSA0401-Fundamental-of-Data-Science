import numpy as np
bed=np.array([4,5,2,5])
sqa=np.array([120,434,23,43])
price=np.array([10000,20000,30000,4000])
avg=price[bed>4]
a=np.mean(avg)
print("Average saleprice of house with more than four bedrooms:",a)
