import pandas as pd
data = ['s','a','t','y','a']
series = pd.Series(data)
print("One-dimensional array-like object (Pandas Series):")
print(series)

import pandas as pd
data = pd.Series(['s','a','t','y','a'])
print("Pandas Series:")
print(data)
py_list = data.tolist()
print("\nConverted to Python list:")
print(py_list)
print("\nType of the converted object:", type(py_list))
