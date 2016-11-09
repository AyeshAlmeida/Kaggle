import csv as csv
import numpy as np

#reading the CSV
csv_file = open('train.csv', 'rb')
csv_file_object = csv.reader(csv_file)
header = csv_file_object.next()

#writing to Genderbased Modal
gender_based_modal = open('gender_based_modal.csv', 'wb')
gender_based_modal_object = csv.writer(gender_based_modal)

#Writing to the gender_based_modal
gender_based_modal_object.writerow(["PassengerId", "Survived"])

for row in csv_file_object:
    if row[4] == 'female':
        print("female")
        gender_based_modal_object.writerow([row[0], '1'])
    else:
        print("male")
        gender_based_modal_object.writerow([row[0], '0'])

csv_file.close()
gender_based_modal.close()




