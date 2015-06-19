
import numpy as np
import pandas as pd
from pymongo import MongoClient
from bokeh.plotting import figure, output_file, show, VBox
import datetime



def dateCount(collection):
    client = MongoClient('140.114.77.18', 27017)
    collection = client['idea'][collection]
    dateCount ={}
    for tweet in collection.find():
        date =  np.datetime64(tweet["created_at"].date().strftime("%Y-%m-%d"))
        dateCount[date] = dateCount.get(date,0) + 1
    return pd.DataFrame(list(dateCount.items())).sort([0])


# Here is some code to read in some stock data from the Yahoo Finance API

BPD_tweets = dateCount('BDP_emotion')


regular_tweets = dateCount('regularUser_en')

output_file("tweets_distribution.html", title="Tweets Distribution")

# create a figure
p1 = figure(title="Tweets",
            x_axis_label="Date",
            y_axis_label="Post Count",
            x_axis_type="datetime")

p2 = figure(title="Tweets",
            x_axis_label="Date",
            y_axis_label="Post Count",
            x_axis_type="datetime")

p1.below[0].formatter.formats = dict(years=['%Y'],
                                     months=['%b %Y'],
                                     days=['%d %b %Y'])


p2.below[0].formatter.formats = dict(years=['%Y'],
                         months=['%b %Y'],
                         days=['%d %b %Y'])

# EXERCISE: finish this line plot, and add more for the other stocks. Each one should
# have a legend, and its own color.
p1.line(
    BPD_tweets[0],                                       # x coordinates
    BPD_tweets[1],                                  # y coordinates
    color='#A6CEE3',                                    # set a color for the line
    legend='BPD People',                                      # attach a legend label
)

p2.line(
    regular_tweets[0],                                       # x coordinates
    regular_tweets[1],                                  # y coordinates
    color='#E09926',                                    # set a color for the line
    legend='Regular People',                                      # attach a legend label
)




# EXERCISE: style the plot, set a title, lighten the gridlines, etc.
p1.title = "BDP Tweets along with Time"
p1.grid.grid_line_alpha=0.3

p2.title = "Regular Tweets along with Time"
p2.grid.grid_line_alpha=0.3

# EXERCISE: start a new figure

# Here is some code to compute the 30-day moving average for AAPL


window_size = 30
window = np.ones(window_size)/float(window_size)

# EXERCISE: plot a scatter of circles for the individual AAPL prices with legend


show(VBox(p1,p2))  # open a browser
