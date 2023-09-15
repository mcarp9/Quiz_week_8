

import matplotlib.pyplot as plt
import pandas as pd

# read the csv data
climateData = pd.read_csv('climate.csv')
print(climateData.head())

years = climateData['Year']
co2 = climateData['CO2']
temp = climateData['Temperature']



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

#savefig means save the figure and show the figure
plt.savefig("q2.png")
plt.show()