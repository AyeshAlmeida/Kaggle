import csv as csv;
import numpy as np;

#reading the CSV
csv_file_object = csv.reader(open('/home/ayesh/Downloads/train.csv', 'rb'));
header = csv_file_object.next();

data = [];
for row in csv_file_object:
    data.append(row);

data = np.array(data);

print(len(data));
print("Hello World!");