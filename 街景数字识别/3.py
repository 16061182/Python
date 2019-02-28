import csv
data0 = []
data45 = []
data90 = []
data135 = []
data180 = []
data225 = []
data270 = []
data315 = []

with open("submission_0.csv","r") as s0:
    reader = csv.reader(s0)
    data0 = [row for row in reader]
    print(len(data0))

with open("submission_45.csv","r") as s45:
    reader = csv.reader(s45)
    data45 = [row for row in reader]
    print(len(data45))
with open("submission_90.csv","r") as s90:
    reader = csv.reader(s90)
    data90 = [row for row in reader]
    print(len(data90))
with open("submission_135.csv","r") as s135:
    reader = csv.reader(s135)
    data135 = [row for row in reader]
    print(len(data135))
with open("submission_180.csv","r") as s180:
    reader = csv.reader(s180)
    data180 = [row for row in reader]
    print(len(data180))
with open("submission_225.csv","r") as s225:
    reader = csv.reader(s225)
    data225 = [row for row in reader]
    print(len(data225))
with open("submission_270.csv","r") as s270:
    reader = csv.reader(s270)
    data270 = [row for row in reader]
    print(len(data270))
with open("submission_315.csv","r") as s315:
    reader = csv.reader(s315)
    data315 = [row for row in reader]
    print(len(data315))

result=open('submission.csv','w', newline='')
writer=csv.writer(result)
print(type(int(data0[0][0])))
print(int(data0[0][0]))

for i in range (0,1800):
    rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    rate[int(data0[i][0])] += 1
    rate[int(data45[i][0])] += 1
    rate[int(data90[i][0])] += 1
    rate[int(data135[i][0])] += 1
    rate[int(data180[i][0])] += 1
    rate[int(data225[i][0])] += 1
    rate[int(data270[i][0])] += 1
    rate[int(data315[i][0])] += 1
    index = rate.index(max(rate))
    print(rate)
    writer.writerow([index])