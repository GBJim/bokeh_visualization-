###
### NOTE: This exercise requires a network connection
###

import numpy as np
import pandas as pd
from pymongo import MongoClient
from bokeh.plotting import figure, output_file, show, VBox
import datetime



def dateCount(collection):
    client = MongoClient('localhost', 27017)
    collection = client['idea'][collection]
    dateCount ={}
    for tweet in collection.find():
        date =  np.datetime64(tweet["created_at"].date().strftime("%Y-%m-%d"))
        dateCount[date] = dateCount.get(date,0) + 1
    return pd.DataFrame(list(dateCount.items()))










# Here is some code to read in some stock data from the Yahoo Finance API

tweetsDate = dateCount('BDP_emotion')
tweetsDate = tweetsDate.sort([0])

AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
IBM = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])

output_file("stocks.html", title="stocks.py example")

# create a figure
p1 = figure(title="Stocks",
            x_axis_label="Date",
            y_axis_label="Close price",
            x_axis_type="datetime")


p1.below[0].formatter.formats = dict(years=['%Y'],
                                     months=['%b %Y'],
                                     days=['%d %b %Y'])

# EXERCISE: finish this line plot, and add more for the other stocks. Each one should
# have a legend, and its own color.
p1.line(
    tweetsDate [0],                                       # x coordinates
    tweetsDate [1],                                  # y coordinates
    color='#A6CEE3',                                    # set a color for the line
    legend='AAPL',                                      # attach a legend label
)


# EXERCISE: style the plot, set a title, lighten the gridlines, etc.
p1.title = "Stock Closing Prices"
p1.grid.grid_line_alpha=0.3

# EXERCISE: start a new figure

# Here is some code to compute the 30-day moving average for AAPL


window_size = 30
window = np.ones(window_size)/float(window_size)

# EXERCISE: plot a scatter of circles for the individual AAPL prices with legend


show(VBox(p1))  # open a browser