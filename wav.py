# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np


# 打开WAV文档
f = wave.open(r"/home/suyu/Downloads/Persona 5 - Life Will Change (中文字幕) (1).wav", "rb")

# 读取格式信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]# (声道数, 量化位数（byte单位）, 采样频率, 采样点数)

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short) #將字串轉換成短整數
wave_data.shape = -1, 2 #行列數 -1,2
wave_data = wave_data.T #轉置
time = np.arange(0, nframes) * (1.0 / framerate)#(0到 nframes)*(1.0/framerate)

# 绘制波形
pl.subplot(211 )#兩行一列,使用位置為1
pl.plot(time, wave_data[0])
pl.subplot(212) #兩行一列,使用位置為2
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()