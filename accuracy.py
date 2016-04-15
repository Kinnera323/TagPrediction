# -*- coding: utf-8 -*-

#This module is incomplete.Look at measures carefully and rewrite.
from classifier import tags_Predicted
from testing_format import tags_actual
from sklearn.metrics import f1_score, precision_score, recall_score

yes = 0
FN = 0
total = 0
got_tags = 0
for actual, predicted in zip(tags_actual, tags_Predicted):
	if set(actual) == set(predicted):
		yes += 1  #True Positve,TP
	elif set(actual) != set(predicted):
		if len(predicted) != 0:
			FN += 1 #Declared wrong tags,false negative (declare H0 when, in truth, H1),	
	if len(predicted) != 0:
		got_tags += 1
	total+=1

P = float(yes*100/got_tags)
R = float(got_tags*100/total)
#print yes,got_tags,total

# Our multi-label classification system’s performance. F1 score is the harmonic mean of precision (the fraction returned results that are correct) and recall (the fraction of correct results that are returned) ##

print "Precision: " ,str(P) # precision_score(actual,predicted,average=None) #
print "Recall: " , str(R) # recall_score(actual,predicted,average=None) 
print "F1 SCORE: " , str(float(2*P*R/(P+R))) #f1_score(actual,predicted,average=None)  #


