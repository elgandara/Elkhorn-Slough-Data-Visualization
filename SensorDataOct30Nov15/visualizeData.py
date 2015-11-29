# Filename: viualizeData.py
# Name: Eliasar Gandara
# Date: 27 November 2015
# Description: Use pandas and matplotlib to visualize the data from the two sensors at Elkorn Slough.

import datetime
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

newSensor = pd.read_csv("newSensorOct31ToNov14.csv")
oldSensor = pd.read_csv("oldSensorOct31ToNov14.csv")

# The format that the date is formatted in the csv files
date_format = "%Y/%m/%d %H:%M"

# Create a "datetime" column that will contain a datetime object to be used in graphing the data sequentially based on the date and time
newSensor["datetime"] = newSensor["DateTime"].apply(lambda x: datetime.datetime.strptime(x, date_format) )
oldSensor["datetime"] = oldSensor["DateTime"].apply(lambda x: datetime.datetime.strptime(x, date_format) )

# Set the x and y label values of the graph
plt.xlabel("Time")
plt.ylabel("Values")

#plt.show()
