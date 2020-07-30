import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

def readAllFile(dir):
    import os
    rootdir = dir
    textList =[]

    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        print(path)
        if os.path.isfile(path):
            try:
                path = path.replace('/','\\')
                # print(path)
                text = open(path, 'r', encoding='gb18030').read()
                textcut = jieba.cut(text)
                s=""
                for word in textcut:
                    s += word + ' '
                    textList.append(s)
                print(s)
            except Exception as e:
                print(e)
    return textList

def classify():
    # 1. 读取停用词
    stop_words = [line.replace('\n','') for line in open('stopword.txt','r',encoding='utf-8').readlines() ]
    # 2. 计算单词权重
    print(stop_words)
    # max_df=0.5表示在50%的文档中都出现过的单词不做为参考标准
    tf=TfidfVectorizer(stop_words=stop_words,max_df=0.5)
    # 3. 加载数据
    tiyu_content = readAllFile('../class21/train/体育')
    tiyu_label = [0 for i in range(0,len(tiyu_content))]
    nvxing_content = readAllFile('../class21/train/女性')
    nvxing_label = [1 for i in range(0, len(nvxing_content))]
    wenxue_content = readAllFile('../class21/train/文学')
    wenxue_label = [2 for i in range(0, len(wenxue_content))]
    xiaoyuan_content = readAllFile('../class21/train/校园')
    print(len(xiaoyuan_content))
    xiaoyuan_label = [3 for i in range(0, len(xiaoyuan_content))]
    train_contents = tiyu_content+nvxing_content+wenxue_content+xiaoyuan_content
    train_labels = tiyu_label+nvxing_label+wenxue_label+xiaoyuan_label
    # 4.生成分词后的单词权重特征空间
    features = tf.fit_transform(train_contents)

    # 5. 生成朴素贝叶斯分类器
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB(alpha=0.001).fit(features, train_labels)
    print(clf)

    # 6. 使用生成的分类器做预测
    # 6.1 加载测试集
    tiyu_content = readAllFile('../class21/test/体育')
    tiyu_label = [0 for i in range(0, len(tiyu_content))]
    nvxing_content = readAllFile('../class21/test/女性')
    nvxing_label = [1 for i in range(0, len(nvxing_content))]
    wenxue_content = readAllFile('../class21/test/文学')
    wenxue_label = [2 for i in range(0, len(wenxue_content))]
    xiaoyuan_content = readAllFile('../class21/test/校园')
    xiaoyuan_label = [3 for i in range(0, len(xiaoyuan_content))]
    test_contents = tiyu_content + nvxing_content + wenxue_content + xiaoyuan_content
    test_labels = tiyu_label + nvxing_label + wenxue_label + xiaoyuan_label

    test_features = tf.transform(test_contents)
    # print(test_features)
    predicted_labels = clf.predict(test_features)
    # 测试准确率
    from sklearn import metrics
    print('准确率为：', metrics.accuracy_score(test_labels, predicted_labels))
if __name__ == '__main__':

    classify()