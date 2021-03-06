# Filename: dataSplitter.py
# Name: Eliasar Gandara
# Date: 24 November 2015
# Description: Will extract the data that the new probe created.
# It will split apart the date, time, temperature, and disolved oxygen readings.

import csv
import datetime

csvfile = open("SensorDataNov14.csv", "r")
new_csvfile = open("newSensorOct31ToNov14.csv", "w")
# reader will allow for the data in the csv file to be read
reader = csv.reader(csvfile)
writer = csv.writer(new_csvfile, delimiter=',')

new_data = []
startDate = datetime.date(2015,10,31)
endDate = datetime.date(2015,11,14)

writer.writerow(["Date", "D.O.", "Temp"])
for row in reader:
    # Split the data in the first column
    data = row[0].split()

    # Add the relevent data to the the new_data list
    # and then write the row to the new csvfile
    new_data.extend( [ data[0] + " " + data[1][0:5], data[3], data[5]] )
    date = datetime.date(int(data[0][0:4]), int(data[0][5:7]), int(data[0][8:]))

    # Will add the row to the csv file if the data is from the appropriate date range
    if (startDate <= date <= endDate):
        writer.writerow( new_data )

    # Reset the values of the new_data list
    new_data = []

# Close the csv files
csvfile.close()
new_csvfile.close()
