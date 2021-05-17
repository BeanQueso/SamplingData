import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print("population mean is:", population_mean)

def randMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataSet.append(value)

    ds_mean = statistics.mean(dataSet)
    ds_stdev = statistics.stdev(dataSet)
    return ds_mean

    #print("mean of the sample data is:", ds_mean)
    #print("the standard deviation of the sample data is:", ds_stdev)

def drawGraph(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    standardDeviation = statistics.stdev(df)
    print("mean of sampling mean distribution is:", mean)
    fig = ff.create_distplot([df], ["Temp"], show_hist = False)
    fig.show()

#function to get mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list = []
    
    for i in range(0,100):
        setOfMean = randMean(30)
        mean_list.append(setOfMean)
    drawGraph(mean_list)

setup()
    
