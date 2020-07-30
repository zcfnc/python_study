from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vec = TfidfVectorizer()
documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)

# 查看每个词的id
print(tfidf_vec.vocabulary_)
# 查看每个词的tf-idf值
print('每个单词的tfidf值:', tfidf_matrix.toarray())
