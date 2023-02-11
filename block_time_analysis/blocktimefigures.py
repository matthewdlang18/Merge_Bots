import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load the data
data = pd.read_csv('blocktimes_raw.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['blocktime'] = data['timestamp'].diff()

#convert blocktime to seconds
data['blocktime'] = data['blocktime'].dt.total_seconds()

#drop data for blocks before 15050001
data = data.loc[data['blocknumber'] >= 15050001]

#group the data by every 1000 blocks and calculate the mean of dif
data_1000 = data.groupby(data['blocknumber']//1000).blocktime.mean()
#calculate the standard deviation of dif every 1000 blocks
data_1000_sd = data.groupby(data['blocknumber']//1000).blocktime.std()

#create a scatter plot of blocktime on the y-axis and number on the x-axis

plt.scatter(data_1000.index/1000, data_1000.values, s = 0.75, c='black')
plt.axvline(x = 15.537393, color = 'b')
plt.text(15.4, 15.7, 'Ethereum Merge', verticalalignment = 'center_baseline', c='b')
plt.xlabel('Block Number (in millions)')
plt.ylabel('Average Block Time (1000 block increments)')
#add a regression line if blockgroup is less than 15.537 and greater than or equal to 15.537


x = data_1000.index/1000
y = data_1000.values

mask = x < 15.537393
x1 = x[mask]
y1 = y[mask]
m1, b1 = np.polyfit(x1, y1, 1)
print(m1, b1)
x2 = x[~mask]
y2 = y[~mask]
m2, b2 = np.polyfit(x2, y2, 1)
print(m2, b2)
plt.plot(x1, m1*x1 + b1, color = 'r', label = 'blockgroup < 15.537')
plt.plot(x2, m2*x2 + b2, color = 'g', label = 'blockgroup >= 15.537')

#save figure
plt.savefig('blocktimeavg.png', dpi = 300)
plt.show()

#create a scatter plot of moving standard deviation of blocktime on the y-axis and number on the x-axis
#do not include if the standard deviation is NaN
data_1000_sd = data_1000_sd.dropna()

plt.scatter(data_1000_sd.index/1000, data_1000_sd.values, s = 0.75, c='black')
plt.axvline(x = 15.537, color = 'b')
plt.text(15.4, 16.7, 'Ethereum Merge', verticalalignment = 'center_baseline', c='b')
plt.xlabel('Block Number (in millions)')
plt.ylabel('Standard Deviation of Block Time (1000 block increments)')
#add a regression line if blockgroup is less than 15.537 and greater than or equal to 15.537
import numpy as np
import matplotlib.pyplot as plt

x = data_1000_sd.index/1000
y = data_1000_sd.values

mask = x < 15.537
x1 = x[mask]
y1 = y[mask]
m1, b1 = np.polyfit(x1, y1, 1)
print(m1, b1)
x2 = x[~mask]
y2 = y[~mask]
m2, b2 = np.polyfit(x2, y2, 1)
print(m2, b2)
plt.plot(x1, m1*x1 + b1, color = 'r', label = 'blockgroup < 15.537')
plt.plot(x2, m2*x2 + b2, color = 'g', label = 'blockgroup >= 15.537')

# save figure so it can be used in latex
plt.savefig('blocktimestd.png', dpi=300)
plt.show()
