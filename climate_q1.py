
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
# Fetch data from the climate.db
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData ORDER BY Year")



#practice code for fetching the table name for climate.db
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

#Practice for fetching the table name in the climate.db
#for table in tables:
    #print(table[0])


#print(tables)

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

plt.savefig("q1.png")
plt.show()