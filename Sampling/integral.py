import numpy as np
'''
\int_{0}^{1} x^{2}dx    gt=0.3333333....
'''
N=10000
x=np.random.uniform(0,1,N)
x=np.square(x)
print(np.mean(x))
