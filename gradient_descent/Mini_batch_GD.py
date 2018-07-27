import numpy as np
# from scipy import stats
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.2)
m = len(x)
print(m)
x0 = np.full(m, 1.0)
# print(x0)
input_data = np.vstack([x0, x]).T
target_data = 2*x + 5 + np.random.random(m)
# print(input_data)
loop_max = 10000
epsilon = 1e-3
np.random.seed(0)
theta = np.random.randn(2)

alpha = 0.001
diff = 0
error = np.zeros(2)
count = 0
finish = 0
minibatch_size = 5
while count < loop_max:
    count += 1
    for i in range(1, m, minibatch_size):
        sum_m = np.zeros(2)
        for k in range(i-1, i+minibatch_size-1, 1):
            dif = (np.dot(theta, input_data[k])-target_data[k])*input_data[k]
            sum_m = sum_m + dif
        theta = theta-alpha*(1.0/minibatch_size)*sum_m
    if np.linalg.norm(theta - error) < epsilon:
        finish = 1
        break
    else:
        error = theta
print('loop count = %d' % count, '\tw', theta)

plt.plot(x, target_data, 'g*')
plt.plot(x, theta[1] * x + theta[0], 'r')
plt.show()
