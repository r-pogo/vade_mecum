# CSV

## Reading with csv module
````python
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
````
Reading CSV Files Into a Dictionary with DictReader, the first row is used as header
````python
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
````
___
## Optional CSV reader Parameters
The reader object can handle different styles of CSV files by specifying additional parameters.
Example:
delimiter specifies the character used to separate each field. The default is the comma (',').

quotechar specifies the character used to surround fields that contain the delimiter character. The default is a double quote (' " ').

escapechar specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.
___
## Writing CSV Files With csv module
````python
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
````
Writing CSV File From a Dictionary DictWriter, the first row is used as header
````python
import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
````
___
## Reading CSV Files With pandas
````python
import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)
````
Reading CSV:
````python
csv_data = pd.read_csv("input.csv")
````
From a CSV file, specifying which columns you want to import:
````python
csv_data = pd.read_csv("input.csv", usecols=['col1', 'col4', 'col5'])
````
From a CSV file with no header:
````python
csv_data = pd.read_csv("input.csv", header=None, names=['colA', 'colB'])
````
From a pipe-delimited file:
````python
pipe_delimited_data = pd.read_csv("input.csv", sep='|')
````
___
## Writing CSV Files With pandas
````python
import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')
````
Saving to CSV:
````python
data.to_csv('output.csv')
````
To CSV files, without the index:
````python
data.to_csv('output.csv', index=False)
````
To pipe-delimited files:
````python
data.to_csv('output.csv', sep='|')
````
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- J. Fincher, Real Python, Reading and Writing CSV Files in Python, https://realpython.com/python-csv/
- Edlitera, Python Pandas Cheat Sheet, https://www.edlitera.com/en/blog/posts/python-pandas-cheat-sheet