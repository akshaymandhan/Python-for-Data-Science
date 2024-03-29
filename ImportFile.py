import pandas as pd
import csv

# Importing File Through Pandas through "import panda"
df = pd.read_csv('HR.csv', parse_dates=['Hire Date'])
print(df)

# OR

# Importing File Through csv through "import csv" & Read PArticular Columns Through Index
with open('efile_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count = line_count + 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count = line_count + 1
print(f'Processed {line_count} lines.')


# Import File through CSV method Read All Data In the File

import csv

with open('HR.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(row)

