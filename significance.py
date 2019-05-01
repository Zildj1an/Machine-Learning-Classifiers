# SIGNIFICANCE TEST (For R)
def columns(file_name, y_pred,y_test):
	f1 = open(file_name, 'w+')

	for i in range(0,len(y_test)): 
		if y_pred[i] == y_test[i]: 
			f1.write("1") 
		else: 
			f1.write("0")
	f1.close
