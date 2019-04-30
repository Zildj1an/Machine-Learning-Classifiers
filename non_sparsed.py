import pandas as pd
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier, Perceptron
from sklearn.naive_bayes import MultinomialNB

############################
# 1 PREPARATION		       #
############################

clickbaits = pd.read_csv("c_fb_post.csv", na_values=['?'])
news = pd.read_csv("n_fb_post.csv", na_values=['?'])

# Feature names
headers_clickbaits = list(clickbaits)
headers_news = list(news)

############################
# 2 DATA EXPLORATION       #
############################

# Column names
print("News Features:")
print(headers_news)
print("Columns in News = ", len(headers_news))

print("Clikbaits Features:")
print(headers_clickbaits)
print("Columns in Clickbaits = ", len(headers_clickbaits), "\n")

# Unique elements of column fb_page
clickbaits_fbpages = set(clickbaits["fb_page"])
print("Unique elems in column fb_page for clickbait = ", clickbaits_fbpages)

news_fbpages = set(news["fb_page"])
print("Unique elems in column fb_page for news = ", news_fbpages, "\n")

############################
# 3 PREPROCESSING          #
############################

# Feature matrix
x = []

# Label Array
y = []

le = preprocessing.LabelEncoder()
le = le.fit(news['post_type'].unique())
for index, row in clickbaits.iterrows():

	vector = [le.transform([row['post_type']])[0], row['num_reaction_cleaned'], row['num_comment_cleaned'], row['num_share_cleaned']]
	#transformed_vector = le.fit_transform(vector) -> This did not work. Dont fit inside the loop.
	x.append(vector)
	y.append('c')

for index, row in news.iterrows():

	vector = [le.transform([row['post_type']])[0], row['num_reaction_cleaned'], row['num_comment_cleaned'], row['num_share_cleaned']]
	x.append(vector)
	y.append('n')

x = numpy.asarray(x)

############################
# 4 CLASSIFICATION         #
############################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
print(x_train.shape)
print(x_test.shape)

# Been a low-dimensional feature set, if Linear SVC fails a good option is KNeighbors.
# If KNeighbors fails, a good alternative is SVM or perhaps ensemble methods (like Bagging).
# Other estimators included that will -most likely- work poorly than KN are Decision trees,Perceptron and MultinomialNB.

# (1) Create the model
SVCclf = LinearSVC()
KNclf  = KNeighborsClassifier()
SVMclf = svm.SVC()
Bagging_clf = BaggingClassifier(KNeighborsClassifier())
DTclf = DecisionTreeClassifier()
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
