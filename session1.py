import urllib.request

import matplotlib.pyplot as plt
import pandas as pd

#reading data from the file 
data_df = pd.read_csv("./slim.csv")
print(data_df)
plt.pie(data_df.Gold,shadow=True, startangle=90, labels=["USA","Britain","China","Russian","Germany"] , explode=(0.02,0.02,0.02,0.02,0.02), colors=["red","green","yellow","black","purple"], autopct="%1.1f%%")
plt.title("Gold medal achievements of the five most successfull countries")
plt.show()

plt.bar(data_df.Name,data_df.Gold, color=["red","green","blue","black","yellow"], label="AWARD")
plt.show()

plt.plot(data_df.Name, data_df.Gold)
plt.show()