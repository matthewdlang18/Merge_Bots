import pandas as pd

#load the data
data = pd.read_csv('blocktimes_raw.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['blocktime'] = data['timestamp'].diff()

#convert blocktime to seconds
data['blocktime'] = data['blocktime'].dt.total_seconds()

#calculate the standard deviation of dif over the last 1000 blocks
sd_dif_10 = data['blocktime'].rolling(window = 10, min_periods = 1).std()
sd_dif_100 = data['blocktime'].rolling(window = 100, min_periods = 1).std()
sd_dif_1000 = data['blocktime'].rolling(window = 1000, min_periods = 1).std()

#store the standard deviation in the data frame
data['sd_dif_10'] = sd_dif_10
data['sd_dif_100'] = sd_dif_100
data['sd_dif_1000'] = sd_dif_1000

#calculate the mean of dif and sd_dif_1000 before and after blockNumber 15537393
before = data.loc[data['blocknumber'] <= 15537393]
after = data.loc[data['blocknumber'] > 15537393]

before_mean = before.mean()
after_mean = after.mean()

#create a table with the average of blocktime, sd_dif_10, sd_dif_100, and sd_dif_1000 before and after blockNumber 15537393
table = pd.DataFrame({'Before': [before_mean['blocktime'], before_mean['sd_dif_10'], before_mean['sd_dif_100'], before_mean['sd_dif_1000']],
'After': [after_mean['blocktime'], after_mean['sd_dif_10'], after_mean['sd_dif_100'], after_mean['sd_dif_1000']]})
table.index = ['blocktime', 'sd_dif_10', 'sd_dif_100', 'sd_dif_1000']
table = table.round(2)
print(table)



#save the table as a csv file
table.to_csv('meanstable.csv')
