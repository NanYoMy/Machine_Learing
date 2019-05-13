import numpy as np

def mc(N):
    hit=0
    for i in range(N):
        x=np.random.uniform(0,1,1)
        y=np.random.uniform(0,1,1)
        if (x*x+y*y)<1.0:
            hit+=1
    print("pi=%f"%(hit/N*4))
mc(10000)