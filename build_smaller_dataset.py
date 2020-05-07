# Read the full dataset from https://github.com/karolzak/support-tickets-classification#22-dataset
# Build a smaller balanced dataset, looking only at body and urgency.

import pandas as pd
from collections import Counter
from collections import defaultdict
import random


df = pd.read_csv("all_tickets.csv")

bodies = df['body'].to_list()
urgencies = df['urgency'].to_list()

remapped = defaultdict(list)

for i, body in enumerate(bodies):
    urg = urgencies[i]
    remapped[urg].append(body)

print(remapped.keys())

for urg in remapped:
    remapped[urg] = remapped[urg][:1500]


bodies = remapped[0] + remapped[1] + remapped[2] + remapped[3]
labels = [0] * 1500 + [1] * 1500 + [2] * 1500 + [3] * 1500



print(len(bodies))
print(len(labels))

combined = list(zip(bodies, labels))
random.shuffle(combined)

bodies, labels = zip(*combined)

print(bodies[1])
print(labels[1])


lab4_out = open("labels_4.txt", "w")
lab2_out = open("labels_2.txt", "w")
with open("tickets.txt", "w") as f:
    for i, body in enumerate(bodies):
        f.write("{}\n".format(body))
        lab4_out.write("{}\n".format(labels[i]))
        if labels[i] in (0, 1):
            label = "urgent"
        elif labels[i] in (2, 3):
            label = "not_urgent"
        else:
            print("UNEXPECTED VALUE")
            print(labels[i])
            print(type(labels[i]))
        lab2_out.write("{}\n".format(label))

    lab4_out.close()
    lab2_out.close()






