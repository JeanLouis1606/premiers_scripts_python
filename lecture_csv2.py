#example de lecture de csv
import csv

with open('age2.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t nom : {row[0]} , prénom : {row[1]} date de naissance : {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')