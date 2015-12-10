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

# Create a new dataframe that contains both of the sensor's data'
#frames = [newSensor, oldSensor]
#bothSensors = pd.concat(frames)

# Make the index of the bothSensors dataframe equal to a datetime object
#bothSensors.index = bothSensors["Date"].apply(lambda x: datetime.datetime.strptime(x, date_format) )

newSensor.index = newSensor["Date"].apply(lambda x: datetime.datetime.strptime(x, date_format) )
oldSensor.index = oldSensor["Date"].apply(lambda x: datetime.datetime.strptime(x, date_format) )

#groups = bothSensors.groupby("Sensor")

#for key, group in groups:
    #group.plot()

newSensor.plot();
oldSensor.plot();

plt.legend(loc="best")

# Display the plot
plt.show()
