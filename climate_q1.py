
import sqlite3
import matplotlib.pyplot as plt

#Created empty list
years = []
co2 = []
temp = []

# Make a connection to the database
con = sqlite3.connect('climate.db')
# Make a cursor to execute SQL queries
cursor = con.cursor()
# Fetch data from the xclimate.db
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData ORDER BY Year")
tables = cursor.fetchall()

for table in tables:
    years.append(table[0])
    co2.append(table[1])
    temp.append(table[2])

con.close()






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
plt.savefig("co2_temp_1.png")
