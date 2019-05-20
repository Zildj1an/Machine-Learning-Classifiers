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

* For non-sparsed data sets (https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/non_sparsed.py), if it is a low-dimensional data set, probably K-Neighbors will work better (comment the other models to speed compilation, omit that technically speaking KNN is example-based and not a model). Otherwise, SGD will probably work well on high-dimensional data sets.

* For sparse data (like the text I used in https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/sparse.py), K-Neighbors is NOT suitable and I suggest Linear SVC or Multinomial-NB.Other good option for low-dimensional text data would be Naive Bayes

* I have tested both situations with the data in csv format and uploaded the reports: https://github.com/Zildj1an/Machine-Learning-Classifiers/tree/master/report.

# Significance and P-Value
Having better report results is not always caused by a better model, but could be just a coincidence. Therefore, it is interesting to discuss the statistical significance of those differences between estimators, computing the P-Value.
Since the data is formed by dependent and paired samples you can use **McNemar's test** in an R script (https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/significance/significance.R), after obtaining the desired column with https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/significance.py).
For instance, I did so between the two best classifiers according to the reports (Naive Bayes and Linear SVC) and obtained:

```
McNemar's Chi-squared test with continuity correction

data:  clf1 and clf2
McNemar's chi-squared = 0.80856, df = 1, p-value = 0.3685
```
In thic case, the p-value is not low enough (>0.05), hence we can NOT safely say that the differences in the results are truly caused by differently performing classifiers (we can't reject the null hypothesis). 

# Visualize the Decision Tree
View line 40 of sparse.py
If it is not overffited it probably can be visualized, and then the .dot file visualized with ```xdg``` and converted with:

```
$ dot -Tpdf tree.dot -o tree.pdf
```

Here I show the decision tree for the sparse data set using a depth of three (others can be found in the folder):

![](https://github.com/Zildj1an/Machine-Learning-Classifiers/blob/master/tree_images/tree.jpg)

