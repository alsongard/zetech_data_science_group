import numpy as np
import pandas as pd
array_1 = np.array(["January","February","March","April"])
# print(array_1)
#use of inclusize and exlcusive

print(array_1[0:3])
print(array_1[:4])


prices = [12,23,14,15.1,16,17.0,18]
earings = [9,5,7,8,9,9,3,5,6,7,7]
earings_np = np.array(earings)
prices_np = np.array(prices)
print(type(prices_np))
print(type(earings_np))

print("Data from the earings_np array: ")
print(earings_np)
print("\n")

print("Data from the prices_np array: ")
print(prices_np)

data = {
    "names": ["Gard", "Alson", "Safari"], 
    "age" : [23, 24, 25]
}
data_df = pd.DataFrame(data)
print(data_df)

data = [["saadia",2,93],
        ["Gard", 3, 94],
        ["Safari", 4, 96]
]
data_df = pd.DataFrame(data, columns=["name","Age","marks"])
print(data_df)