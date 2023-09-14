import matplotlib.pyplot as plt
import pandas as pd


climateData = pd.read_csv('climate.csv')

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
plt.show() 
plt.savefig("co2_temp_2.png")

plt.savefig("co2_temp_2.png")

plt.show()