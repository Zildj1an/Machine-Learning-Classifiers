# change the directory
getwd()
table_1 = read.table('mnb_columns',header=FALSE) 
table_2 = read.table("svc_column", header=FALSE)
clf1 = table_1[[1]] 
clf2 = table_2[[1]]
 
if(length(clf1) > length(clf2)) {
      clf1 <- head(clf1,n = length(clf2))
}
if(length(clf1) < length(clf2)){
      clf2 <- head(clf2,n = 0:length(clf1))
}

mcnemar.test(clf1,clf2)
