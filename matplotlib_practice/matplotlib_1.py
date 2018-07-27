from pylab import *
import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
figure(figsize=(6, 4), dpi=80)
subplot(1, 1, 1)
plot(X, C, color='blue', linewidth=2.0, linestyle='-')
plot(X, S, color='red', linewidth=2.0, linestyle='-')
xticks(np.linspace(-4, 4, 9, endpoint=True))
yticks(np.linspace(-1, 1, 5, endpoint=True))
savefig('matplotlib.png', dpi=80)
show()
