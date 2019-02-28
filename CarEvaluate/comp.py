import csv
import numpy as np

with open('submission.csv','r') as s_file:
    reader = csv.reader(s_file)
    s_data = np.array([row for row in reader])
with open('bsubmission.csv','r') as b_file:
    reader = csv.reader(b_file)
    b_data = np.array([row for row in reader])

print(b_data)
k = 0
for i in range(0,518):
    if s_data[i][0] != b_data[i][0]:
        k += 1
        print(k,': At line ',i,' find ',s_data[i][0],' but b is ',b_data[i][0])