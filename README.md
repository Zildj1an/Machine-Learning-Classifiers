# Machine-Learning-Classifier
Chose the one that best fits your data set: low-dimensional, high-dimensional, or sparsed.

* The following estimators are used:
  + Linear SVC
  + K-Neighbors (most likely will show the best results at the report for your data if low-dimensional)
  + Support Vector Machine
  + Bagging (Ensemble method)
  + Decission Tree
  
  Additionaly, other three classifiers are tested:
  
  + Perceptron
  + SGD (most likely will show the best results at the report for your data if high-dimensional, i.e. more than 100k samples)
  + Multinomial-NB

* For non-sparsed data sets (https://github.com/Zildj1an/Machine-Learning-Classifier/blob/master/non_sparsed.py), if it is a low-dimensional data set, probably K-Neighbors will work better (comment the other models to speed compilation). Otherwise, SGD will probably work well on high-dimensional data sets.

* For sparse data, K-Neighbors is NOT suitable and I suggest Linear SVC (review the reports).Other good option for low-dimensional text data would be Naive Bayes
