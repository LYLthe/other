from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E:\MATLABproject\Sound_Data\异物数据\Record2.wav'
sampfreq, snd = wavfile.read(file_path)
s1 = snd[:, 0]
s2 = snd[:, 1]
N = snd.shape[0]
time = np.arange(0, N) * (1.0 / sampfreq)
# timeArray = range(0, 777592.0, 1)
# timeArray = timeArray / sampfreq
# timeArray = timeArray * 1000
plt.subplot(211)
plt.plot(time, s1)
plt.subplot(212)
plt.plot(time, s2)
plt.show()
