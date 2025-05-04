import pandas as pd
pd.plotting.register_matplotlib_converters()    #ensures smooth integration between Pandas' datetime handling and Matplotlib's plotting capabilities. It's often a necessary step when working with time series data in Pandas and Matplotlib.
import matplotlib.pyplot as plt
import seaborn as sns

'''
The dataset for this tutorial tracks global daily streams on the music streaming service Spotify. 
We focus on five popular songs from 2017 and 2018:
'''

#Load the dataset
filepath = "./data/spotify.csv"
spotify_data = pd.read_csv(filepath, index_col="Date", parse_dates=True)   #By (index_col="Date", The index of a DataFrame provides a label for each row based on the "Date" column. By (parse_dates=True), tells Pandas to attempt to parse any column that looks like a date or time into a Pandas DatetimeIndex or Timestamp objects.


#Examine data
print(spotify_data.head())          #Empty entries will appear as NaN, which is short for "Not a Number".
print(spotify_data.tail())


# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)             #To create a lineplot
plt.show()


#Line chart/plot with additional details
    # Set the width and height of the figure
plt.figure(figsize=(14,6))
    # Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
    # Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)
plt.show()


#Plot a subset of the data
    #View the columns
print(list(spotify_data.columns))
    # Set the width and height of the figure
plt.figure(figsize=(14,6))
    # Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
    # Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
    # Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
    # Add label for horizontal axis
plt.xlabel("Date")
plt.show()


# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")   #By  label="Shape of You", to make the line appear in the legend and set its corresponding label.
plt.show()
