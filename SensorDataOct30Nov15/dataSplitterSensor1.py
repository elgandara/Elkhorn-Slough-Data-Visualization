# Filename: dataSplitterSensor1.py
# Name: Eliasar Gandara
# Date: 25 November 2015
# Description: Parse through the Elkorn Slough data to extract the
# relevant information.


import csv
import datetime

csvfile = open("ELKSMWQ.csv", "r")
new_csvfile = open("oldSensorOct31ToNov14.csv", "w")
# reader will allow for the data in the csv file to be read
reader = csv.reader(csvfile)
writer = csv.writer(new_csvfile, delimiter=',')

new_data = []
startDate = datetime.date(2015,10,31)
endDate = datetime.date(2015,11,14)

writer.writerow(["Date", "D.O.", "Temp"])

for row in reader:

    if row:
        if (row[0] == "elksmwq"):

            # Add the relevent data to the the new_data list
            # and then write the row to the new csvfile
            data = row[2].split()

            date = datetime.date(int(data[0][6:]), int(data[0][:2]), int(data[0][3:5]))
            date_str = date.strftime("%Y/%m/%d")

            new_data.extend( [date_str + " " + data[1], row[12], row[6]] )

            # Will add the row to the csv file if the data is from the appropriate date range
            if (startDate <= date <= endDate):
                writer.writerow( new_data )

    # Reset the values of the new_data list
    new_data = []

# Close the csv files
csvfile.close()
new_csvfile.close()
