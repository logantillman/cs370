# Author: Logan Tillman
# NetID: Ltillma4
# Hw1
 
import matplotlib
from numpy import arange
import matplotlib.pyplot as plt

xData = arange(1,32)
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = []

# Initializing the sum to 0 so I can keep a running average
sum = 0

print(' Day     Avg')
print('______________')

# Calculating the running average for the temperature data
for i, temp in enumerate(tData):
    sum += temp
    
    # Appending the average to the avg list
    avg.append(sum / (i+1))
    
    # Table formatting
    print('|', '{:2d}'.format(i+1), '|', '{:.2f}'.format(sum / (i+1)), '|')
    
# Plotting the original data
plt.plot(xData, tData, color='blue', marker='o', mfc='red', mec='black')

# Plotting the Averages data
plt.plot(xData, avg, color='green', ls='dashed')

# Setting the x and y limits
plt.xlim(0, 32)
plt.ylim(70, 95)

# Enabling the grid
plt.grid(ls='--')

# Setting the title and axis labels
plt.title('High Temperatures for Knoxville, TN - August 2013')
plt.xlabel('Day')
plt.ylabel('High Temp')

# Labeling the monthly average line
matplotlib.pyplot.text(15, 86,'Monthly Avg', color='green')

plt.show()