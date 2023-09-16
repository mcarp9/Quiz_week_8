

import matplotlib.pyplot as plt
import pandas as pd

# read the csv data
climateData = pd.read_csv('climate.csv')
#using anaconda prompt, cd to file location
#show the data of years
print(climateData.head())

#extract the datas in the columns in order, (years, co2 and temp)
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

#savefig means save the figure and show means show the figure
plt.savefig("q2.png")
plt.show()