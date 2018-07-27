import matplotlib.pyplot as plt
import numpy as np
from read_signal import waveread
file_path = 'E:\MATLABproject\Sound_Data\异物数据\Record2.wav'
data, time, fs, nfs = waveread(file_path)

df = fs/(nfs-1)
freq = [df*n for n in range(0, nfs)]
transformed = np.fft.fft(data[0])
d = int(len(transformed)/2)

while freq[d] > 5000:
    d -= 10
freq = freq[:d]
transformed = transformed[:d]
for i, data in enumerate(transformed):
    transformed[i] = abs(data)
plt.subplot(212)
plt.plot(freq, np.real(transformed), 'b-')
plt.xlabel('Freq/Hz')
plt.ylabel('Ampltitude')
plt.show()

# plt.subplot(211)
# plt.plot(time, data[0])
# plt.subplot(212)
# plt.plot(time, data[1], c="g")
# plt.xlabel("time (seconds)")
# plt.show()
