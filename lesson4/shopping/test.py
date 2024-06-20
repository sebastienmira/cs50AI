from shopping import *
evidence = []
labels = []
with open('/home/sedesocamira/cs50ai/lesson4/shopping/shopping.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        evidence.append(row[:17])
        
        if row[17] == 'TRUE':
            labels.append(1)
        else:
            labels.append(0)

#print(evidence[1])
evidence.pop(0)
labels.pop(0)

labels_labels=['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay', 'Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend']
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for row in evidence:

    for i in [1,3,5,6,7,8,9]:
        row[i] = float(row[i])

    for i in [0,2,4,11,12,13,14]:
        row[i] = int(row[i])

    row[10] = months.index(row[10])

    if row[15] == 'Returning_Visitor':
        row[15] = 1
    else:
        row[15] = 0

    if row[16] == 'TRUE':
        row[16] = 1

    else:
        row[16] = 0


print(evidence[0])
print(labels[0])


model = KNeighborsClassifier(n_neighbors=1)

print(model.fit(evidence, labels).score(evidence, labels))