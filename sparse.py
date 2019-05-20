import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier, Perceptron
from sklearn.naive_bayes import MultinomialNB

def model(X,y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    # print(x_train.shape)
    # print(x_test.shape)
  
   # You could just use an array of estimators but I rather this way for modifying specific fits, removing parts...

    # (1) Create the model
    SVCclf = LinearSVC()
    KNclf  = KNeighborsClassifier()
    SVMclf = svm.SVC()
    Bagging_clf = BaggingClassifier(KNeighborsClassifier())
    DTclf = DecisionTreeClassifier(max_depth=7)
    Pclf = Perceptron()
    SGDclf = SGDClassifier()
    MNBclf = MultinomialNB()

    # (2) Fit the model
    SVCclf.fit(x_train, y_train)
    KNclf.fit(x_train, y_train)
    SVMclf.fit(x_train, y_train)
    Bagging_clf.fit(x_train,y_train)
    DTclf.fit(x_train, y_train)
    Pclf.fit(x_train, y_train)
    SGDclf.fit(x_train, y_train)
    MNBclf.fit(x_train, y_train)

    # Visualize the tree
    # For open: dot -Tpdf tree.dot -o tree.pdf
    # Requires imports: 
    #from sklearn.datasets import load_iris
    #from sklearn import tree
    #iris = load_iris()
    #DTclf = DTclf.fit(x_train, y_train)
    #tree.export_graphviz(DTclf, out_file='tree.dot')
    
    # (3) Predict
    SVCy_pred     = SVCclf.predict(x_test)
    KNy_pred      = KNclf.predict(x_test)
    SVMy_pred     = SVMclf.predict(x_test)
    Baggingy_pred = Bagging_clf.predict(x_test)
    DTy_pred      = DTclf.predict(x_test)
    Py_pred       = Pclf.predict(x_test)
    SGDy_pred     = SGDclf.predict(x_test)
    MNBy_pred     = MNBclf.predict(x_test)
    #print(KNy_pred)

    # (4) Report results
    print("SVC REPORT:")
    print(classification_report(y_test, SVCy_pred))
    print("")
    print("KN REPORT (most likely better):")
    print(classification_report(y_test, KNy_pred))
    print("")
    print("SVM REPORT:")
    print(classification_report(y_test, SVMy_pred))
    print("")
    print("BAGGING REPORT:")
    print(classification_report(y_test, Baggingy_pred))
    print("")
    print("DECISION TREE REPORT:")
    print(classification_report(y_test, DTy_pred))
    print("")
    print("PERCEPTRON REPORT:")
    print(classification_report(y_test, Py_pred))
    print("")
    print("SGD REPORT:")
    print(classification_report(y_test, SGDy_pred))
    print("")
    print("MULTINOMIAL-NB REPORT:")
    print(classification_report(y_test, MNBy_pred))


############################
# 1 PREPARATION		       #
############################

news = pd.read_csv("n_fb_post.csv", na_values=['?'])
clickbait = pd.read_csv("c_fb_post.csv", na_values=['nan'])

# Feature matrix
X = []

# Label Array
y = []

# Text array
texts = []

############################
# 2 PREPROCESSING          #
############################

for index, row in news.iterrows():
    if isinstance(row["status_message_without_tags"],str):
        texts.append(row["status_message_without_tags"])
        y.append('n')

for index, row in clickbait.iterrows():
    if isinstance(row["status_message_without_tags"],str):
        texts.append(row["status_message_without_tags"])
        y.append('c')

# min_df is the minimum frequency
word_vectorizer = CountVectorizer(analyzer='word', min_df=4)
X = word_vectorizer.fit_transform(texts)
#print("Shape of X: ", X.shape)
#print("Vocabulary", word_vectorizer.vocabulary_)
#print("Vocabulary length = ", len(word_vectorizer.vocabulary_))

# 'Normalize' the count matrix X (precisely scale down the impact of higher frequency ones)
tfid = TfidfTransformer()
X_normalized = tfid.fit_transform(X)


#####################################################
# 3 CLASSIFICATION FOR RAW X AND X NORMALIZED       #
#####################################################

model(X,y)

# But normalized measures of precision and recall improve

model(X_normalized,y)

# def feature_extraction(text):
#    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
#    extracted_features = [len(text), text.count('!'), len(urls)]
#    return extracted_features

