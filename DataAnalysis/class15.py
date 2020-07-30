import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def class15():
    crashes = sns.load_dataset('car_crashes')
    print(crashes.head(10))
    # 用Seaborn画成对关系,所有属性的二元对比关系
    # sns.pairplot(crashes)
    # 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
    sns.jointplot(x="alcohol", y="total", data=crashes, kind='scatter')
    sns.jointplot(x="alcohol", y="total", data=crashes, kind='kde')
    sns.jointplot(x="alcohol", y="total", data=crashes, kind='hex')
    plt.show()


if __name__ == '__main__':
   class15()