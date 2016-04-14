from classifier import tags_Predicted
from testing_format import tags_actual

yes = 0
total = 0
for actual, predicted in zip(tags_actual, tags_Predicted):
	if set(actual) == set(predicted):
		yes += 1
	total+=1

print yes,total
print "Accuracy: " + str(yes*100/total)