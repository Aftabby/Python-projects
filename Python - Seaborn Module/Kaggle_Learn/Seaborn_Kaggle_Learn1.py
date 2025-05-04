import pandas as pd
pd.plotting.register_matplotlib_converters()    #ensures smooth integration between Pandas' datetime handling and Matplotlib's plotting capabilities. It's often a necessary step when working with time series data in Pandas and Matplotlib.
import matplotlib.pyplot as plt
import seaborn as sns

'''
In this notebook, we'll work with a dataset of historical FIFA rankings for six countries: 
Argentina (ARG), Brazil (BRA), Spain (ESP), France (FRA), Germany (GER), and Italy (ITA).
'''

#Load the dataset
filepath = "./data/fifa.csv"
fifa_data = pd.read_csv(filepath, index_col="Date", parse_dates=True)   #By (index_col="Date", The index of a DataFrame provides a label for each row based on the "Date" column. By (parse_dates=True), tells Pandas to attempt to parse any column that looks like a date or time into a Pandas DatetimeIndex or Timestamp objects.

#Examine data
print(fifa_data.head())

#Plot the data
    # Set the width and height of the figure
plt.figure(figsize=(16,6))
    # Line chart showing how FIFA rankings evolved over time - Line Plot
sns.lineplot(data=fifa_data)
plt.show()

