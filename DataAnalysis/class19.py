import pandas as pd
import numpy as np
import sklearn


train_data = pd.read_csv('./data/class19/c19train.csv')
test_data = pd.read_csv('./data/class19/c19test.csv')
# titles
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
# 1. 缺失值处理
# Age列的缺失值用均值填充
train_data['Age'].fillna(train_data['Age'].mean(),inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)

# Fare列的缺失值用均值填充
train_data['Fare'].fillna(train_data['Fare'].mean(),inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

# 非数值型缺失值的补全
# Embarked为登录港口,查看有哪些值。value_counts按key来group by计数，然后填补缺失值
# 这里有两个空值，用最多的S值补全
# S    644
# C    168
# Q     77
# NaN      2
train_data['Embarked'].fillna('S',inplace=True)

# 2. 特征选择
# PassengerId 为乘客编号，对分类没有作用，可以放弃；
# Name 为乘客姓名，对分类没有作用，可以放弃；Cabin 字段缺失值太多，可以放弃；
# Ticket 字段为船票号码，杂乱无章且无规律，可以放弃。
# 其余的字段包括：Pclass、Sex、Age、SibSp、Parch 和 Fare，
# 这些属性分别表示了乘客的船票等级、性别、年龄、亲戚数量以及船票价格，
# 能会和乘客的生存预测分类有关系。具体是什么关系，我们可以交给分类器来处理。
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
test_labels = train_data['Survived']

# 2.1 将字符型特征数值化
print(train_features[0:5])
from sklearn.feature_extraction import DictVectorizer
dvec=DictVectorizer(sparse=False)

## 2.1.1 特征指定数值化S->1，C->2,Q->0
# test_features['Sex'] = test_features['Sex'].map(lambda x:1 if x=='male' else 0)
# def change(x):
#     if x=='S':
#         return 1
#     elif x=='C':
#         return 2
#     elif x=='Q':
#         return 0
# test_features['Embarked'] = test_features['Embarked'].map(lambda x:change(x))
## 2.1.1 特征分裂数值化
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

print(train_features)


# 3.构建模型
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features,train_labels)


test_features=dvec.transform(test_features.to_dict(orient='record'))
pred_labels = clf.predict(test_features)
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score准确率为 %.4lf' % acc_decision_tree)
# 4. 使用自带的cross_val_score方法进行交叉验证，一般取10次
import numpy as np
from sklearn.model_selection import cross_val_score
# 使用K折交叉验证 统计决策树准确率
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))
