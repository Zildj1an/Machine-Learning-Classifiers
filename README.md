# Machine-Learning-Classifiers
Chose the one that best fits your data set: low-dimensional, high-dimensional, or sparsed.

* The following eight estimators are used:
  + Linear SVC
  + K-Neighbors 
  + Support Vector Machine
  + Bagging (Ensemble method)
  + Decission Tree
  + Perceptron
  + SGD 
  + Multinomial-NB

* For non-sparsed data sets (https://github.com/Zildj1an/Machine-Learning-Classifier/blob/master/non_sparsed.py), if it is a low-dimensional data set, probably K-Neighbors will work better (comment the other models to speed compilation). Otherwise, SGD will probably work well on high-dimensional data sets.

* For sparse data, K-Neighbors is NOT suitable and I suggest Linear SVC (review the reports).Other good option for low-dimensional text data would be Naive Bayes
