import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load the data
data = pd.read_csv('6B40transactions.csv')
data['blockgroup'] = pd.to_numeric(data['blockgroup'])
data['cumprofit'] = data['profit'].cumsum()

#create a scatter plot

x = data['blockgroup'] / 1000
y = data['txn']

mask = x < 15.537
x1 = x[mask]
y1 = y[mask]
m1, b1, c1 = np.polyfit(x1, y1, 2) # change the order of the polynomial fit to 2
print(m1, b1, c1)
x2 = x[~mask]
y2 = y[~mask]
m2, b2, c2 = np.polyfit(x2, y2, 2) # change the order of the polynomial fit to 2
print(m2, b2, c2)

# Generate points along the regression line
x_reg = np.linspace(x.min(), x.max(), 100)
y1_reg = m1*x_reg**2 + b1*x_reg + c1
y2_reg = m2*x_reg**2 + b2*x_reg + c2

# Filter x_reg and y1_reg for blockgroup < 15.537
mask = x_reg < 15.537
x_reg1 = x_reg[mask]
y1_reg1 = y1_reg[mask]

# Filter x_reg and y2_reg for blockgroup >= 15.537
x_reg2 = x_reg[~mask]
y2_reg2 = y2_reg[~mask]

plt.scatter(x, y, s = 0.65, c='black', alpha=0.5)
plt.axvline(x = 15.537, color = 'blue')
plt.text(15.39, 225, 'Ethereum Merge', verticalalignment = 'center_baseline', c='blue')
plt.xlabel('Block Number (in millions)')
plt.ylabel('Transactions per 1,000 Blocks')


plt.plot(x_reg1, y1_reg1, color = 'r', label = 'blockgroup < 15.537')
plt.plot(x_reg2, y2_reg2, color = 'g', label = 'blockgroup >= 15.537')

#add a line of the cumulative profit and have the y-axis on the right
ax2 = plt.twinx()
ax2.plot(x, data['cumprofit'], color = 'orange', label = 'Cumulative Profit')
ax2.set_ylabel('Cumulative Profit (in ETH)', color = 'orange')
plt.savefig('6B40_profit_figure.png', dpi = 300)
plt.show()
