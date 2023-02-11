import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#load the data
data = pd.read_csv('uniswapdailyvolume.csv')
data['date'] = pd.to_datetime(data['date'])
data['cumvolume'] = data['volume'].cumsum()

#create a scatter plot

x = data['date']
y = data['volume']
y2 = data['cumvolume']

plt.scatter(x, y, s = 0.85, c='black', alpha=0.5)
plt.axvline(x = pd.to_datetime('06sep2022'), color = 'blue')
plt.text(pd.to_datetime('2022-08-15'), 6.5e9, 'Ethereum Merge', verticalalignment = 'center_baseline', c='blue')
plt.text(pd.to_datetime('2022-10-30'), 6.5e9, 'FTX Fallout', verticalalignment = 'center_baseline', c='red')
plt.xlabel('Date')
plt.ylabel('Daily Volume (in $)')
#alter the y-axis to billions
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}B'.format(x/1e9)))

# add a line of the cumulative profit and have the y-axis on the right
ax2 = plt.twinx()
ax2.plot(x, y2, color = 'orange', label = 'Cumulative Volume')

# format y-axis to billions
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}B'.format(x/1e9)))
# format the left y-axis to billions
ax2.set_ylabel('Cumulative Volume (in $)', color = 'orange')
plt.savefig('uniswap_daily_volume.png', dpi = 300)
plt.show()
