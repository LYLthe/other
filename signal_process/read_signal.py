import numpy as np
import wave


def waveread(path):
    f = wave.open(path, 'rb')
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    wave_data = np.fromstring(str_data, dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))
    wave_data.shape = -1, 2
    # 将其转置得到：
    wave_data = wave_data.T
    time = np.arange(0, nframes) * (1.0 / framerate)
    return wave_data, time, framerate, nframes


# file_path = 'E:\MATLABproject\Sound_Data\异物数据\Record2.wav'
# f = wave.open(file_path, 'rb')
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# str_data = f.readframes(nframes)
# f.close()
# wave_data = np.fromstring(str_data, dtype=np.short)
# wave_data.shape = -1, 2
# # 将其转置得到：
# wave_data = wave_data.T
# time = np.arange(0, nframes) * (1.0 / framerate)
# plt.subplot(211)
# plt.plot(time, wave_data[0])
# plt.subplot(212)
# plt.plot(time, wave_data[1], c="g")
# plt.xlabel("time (seconds)")
# plt.show()
