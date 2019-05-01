# Machine-Learning-Classifiers
Chose the one that best fits your data set: low-dimensional, high-dimensional, or sparsed.

* The following eight estimators are used:
  + Linear SVC
  + K-Neighbors 
  + Support Vector Machine
  + Bagging (Ensemble method)
  + Decision Tree
  + Perceptron
  + SGD 
  + Multinomial-NB

* For non-sparsed data sets (https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/non_sparsed.py), if it is a low-dimensional data set, probably K-Neighbors will work better (comment the other models to speed compilation). Otherwise, SGD will probably work well on high-dimensional data sets.

* For sparse data (like the text I used in https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/sparse.py), K-Neighbors is NOT suitable and I suggest Linear SVC or Multinomial-NB.Other good option for low-dimensional text data would be Naive Bayes

* I have tested both situations with the data in csv format and uploaded the reports: https://github.com/Zildj1an/Machine-Learning-Classifiers/tree/master/report.

# Significance and P-Value
Having better report results is not always caused by a better model, but could be just a coincidence. Therefore, it is interesting to discuss the \textbf{significance} of those differences between estimators, computing the P-Value.
Since the data is formed by dependent and paired samples I used \textbf{McNemar's test} in an R script (after obatining the desired column with significance.py)
