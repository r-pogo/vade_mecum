# Pandas
Table of content
- [Loading data into Pandas](#loading-data-into-pandas)
- [Reading data in Pandas](#reading-data-in-pandas)
- [Sorting, filtering and describing data](#sorting-filtering-and-describing)
- [Applying changes to the data](#applying-changes-to-the-data)
- [Saving the data](#saving-the-data)
- [Resetting Index](#resetting-index)
- [Regex filtering and string searches](#regex-filtering-and-string-searches)
- [Conditional changes](#conditional-changes)
- [Groupby](#groupby)
- [Chunking large amount of data](#chunking-large-amount-of-data)
## Loading data into Pandas <div id='loading-data-into-pandas'/>
```python
import pandas as pd

db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1) # useful key word arguments
print(df)
print(df.head(3))
print(df.tail(3))
```
___
## Reading data in Pandas <div id='reading-data-in-pandas'/>
Read Headers
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
print(df.columns)
```
Read each Column
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
print(df["name_of_column"][0:5]) # specifying first 5 items
```
Read each row
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
print(df.iloc[1:4]) # iloc = integer location

#Or
for index, row in df.iterrows():
    print(index, row['Name'])

#Or
# df.loc used to look for data on textual, numerical information
df.loc[df['Col_name'] == 'Value_searched']

```
Read a specific location (row, column)
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
print(df.iloc[2,3])
```
___
## Sorting, filtering and describing data <div id='sorting-filtering-and-describing'/>
Describing
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
df.describe()
```
Sorting
```python
import pandas as pd

db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
df.sort_values('Name', ascending=False) # can use multiple columns to sort by
```
Filtering
```python
import pandas as pd

db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)
# with two conditions &== and |== or
df.loc[(df['Col_name'] == 'Value_searched') & (['Col_name'] == 'Value_searched')
        | (['Col_name'] > 100]
```
___
## Applying changes to the data <div id='applying-changes-to-the-data'/>
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

df['New_column'] = df['Stuff'] + df['Stuff2'] + df['Stuff3'] # creating, add at the end
df = df.drop(columns=['New_column']) # deleting
```
Rearranging columns
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

col = list(df.columns.values) # creating a list with col names
df = df[col[0:4] + [col[-1] + col[4:10]]] # moving las col to the middle
```
___
## Saving the data <div id='saving-the-data'/>
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

col = list(df.columns.values) # creating a list with col names
df = df[col[0:4] + [col[-1] + col[4:10]]] # moving las col to the middle

df.to_csv('new_file.csv')
df.to_excel('new_file.xlsx')
df.to_csv('new_file.txt', index=False, sep='\t')
```
___
## Resetting Index resetting-index
When you manipulate the data frame the index stays the same, so it could be useful to  
reset it.
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

new_df = df.loc[(df['Col_name'] == 'Value_searched') & (['Col_name'] == 'Value_searched')]

result = new_df.reset_index(drop=True) # drop to delete all index, otherwise it will be added as a new column
```
___
## Regex filtering and string searches <div id='regex-filtering-and-string-searches'/>
```python
import re
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

df.loc[df['Col name'].str.contains('String searched')]
df.loc[~df['Col name'].str.contains('String searched')] # ~ == not
df.loc[df['Col name']].str.contains('regex | search', flags=re.IGNORECASE ,regex=True)]
```
___
## Conditional changes <div id='conditional-changes'/>
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

df.loc[df['Price'] = 50, 'Price'] = 100
df.loc[df['Total'] > 50, ['Price', 'Amount']] = 100
```
___
## Groupby <div id='groupby'/>
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, encoding="windows-1250", sep=";", skiprows=1)

df.groupby(['Col name']).mean().sort_values('Value', ascending=False)
```
___
## Chunking large amount of data <div id='chunking-large-amount-of-data'/>
```python
import pandas as pd
db = r"path/to/csv/file"
df = pd.read_csv(db, chunksize=5)

for df in pd.read_csv(db, chunksize=5):
    print("CHUNK")
    print(df)

```
___
## Sources
- Pandas documentation, https://pandas.pydata.org/docs/user_guide/index.html
