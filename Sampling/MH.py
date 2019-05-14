import random
import math
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
#matplotlib inline
T = 5000
x = [0 for i in range(T)]
sigma = 1
t = 0

def balance_dist_prob(theta):
    y = norm.pdf(theta, loc=3, scale=2)
    return y

def transfer_dist_prob(x_t,x_t_minu_1):
    return norm.pdf(x_t,loc=x_t_minu_1,scale=sigma)

binom_sim = data = stats.binom.rvs(n=10,p=0.3,size=10000)

while t < T-1:
    t = t + 1
    x[t] = norm.rvs(loc=x[t - 1], scale=sigma, size=1, random_state=None)[0]#q proposal distribution
    #
    alpha = min(1, ((balance_dist_prob(x[t])*transfer_dist_prob(x[t],x[t-1])) / (balance_dist_prob(x[t - 1])*transfer_dist_prob(x[t-1],x[t]))))

    u = random.uniform(0, 1)
    if u > alpha:
        x[t] = x[t - 1]

plt.scatter(x, norm.pdf(x, loc=3, scale=2))
num_bins = 50
plt.hist(x, num_bins, density=1, facecolor='red', alpha=0.7)
plt.show()