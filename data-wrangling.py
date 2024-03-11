import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data = {
    "name": ["allan", "sebu", "macklin","Joa", "christine", "Mike" ],
    "age" : [30,22,28,24,34,19],
    "gender" : ["male", "female", "female", "male", "female", "male"],
    "marks" : [85, 92, np.nan, 88, np.nan, 80]
}
print(data)
print(type(data))
print(data.items())
print("\n")
for key , value in data.items():
    print(f"{key} : {value}")

print("\n")
print(len(data["name"]))
print(len(data["age"]))
print(len(data["gender"]))
print(len(data["marks"]))


mydata = pd.DataFrame(data)
print(mydata)

#drop rows with missing values
# print(mydata.dropna())

#drop columns
print(mydata.dropna(axis=1))

label_encoder = LabelEncoder()
mydata["gender"]  = label_encoder.fit_transform(mydata["gender"])
print(mydata)
# bool_series = pd.isnull(mydata)
# print(bool_series)
