import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def class11():
    data = pd.read_csv("data.csv").dropna()
    print(data)

    data['food'] = data['food'].str.lower()
    data['animal'] = data['food'].str.lower()
    data['ounces'] = data['ounces'].apply(lambda a: abs(a))
    data.drop_duplicates(['food'],inplace=True)

    print(data)



if __name__ == '__main__':
    class11()
