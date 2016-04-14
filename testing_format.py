# import csv

# body_test = []
# tags_actual = []
# with open('TEST.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#     	body_test.append(row[1])
#     	tags_actual.append(row[2])

# f.close()

from training_format import BODY,final_tag,hp

body_test = BODY[hp:]
tags_actual = final_tag[hp:]
