# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_squared_error,mean_absolute_error
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.datasets import load_iris,load_boston,load_digits
# 准备数据集
# 鸢尾花预测
def iris():
    iris=load_iris()
    # 获取特征集和分类标识
    features = iris.data
    labels = iris.target
    print(features)
    print(labels)
    # 随机抽取33%的数据作为测试集，其余为训练集
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
    # 创建CART分类树
    clf = DecisionTreeClassifier(criterion='gini')
    # 拟合构造CART分类树
    clf = clf.fit(train_features, train_labels)
    # 用CART分类树做预测
    test_predict = clf.predict(test_features)
    # 预测结果与测试集结果作比对
    score = accuracy_score(test_labels, test_predict)
    print("CART分类树准确率 %.4lf" % score)
# 波士顿房价预测
def boston():
    # 准备数据集
    boston = load_boston()
    # 探索数据
    print(boston.feature_names)
    print(boston.data)
    # 获取特征集和房价
    features = boston.data
    prices = boston.target
    # 随机抽取33%的数据作为测试集，其余为训练集
    train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33)
    # 创建CART回归树
    dtr = DecisionTreeRegressor()
    # 拟合构造CART回归树
    dtr.fit(train_features, train_price)
    # 预测测试集中的房价
    predict_price = dtr.predict(test_features)
    # 测试集的结果评价
    print('回归树二乘偏差均值:', mean_squared_error(test_price, predict_price))
    print('回归树绝对值偏差均值:', mean_absolute_error(test_price, predict_price))

# 手写数字数据集分类
def digits():

    digits = load_digits()
    features = digits.data
    target = digits.target
    train_features, test_features, train_digit, test_digit = train_test_split(features, target, test_size=0.33)
    # 拟合构造CART分类树
    clf = DecisionTreeClassifier(criterion='gini')
    # 拟合数据模型
    print(type(train_features))
    clf.fit(train_features, train_digit)
    predict_digit = clf.predict(test_features)

    score = accuracy_score(test_digit, predict_digit)
    print("CART分类树准确率 %.4lf" % score)

if __name__ == '__main__':
    digits()