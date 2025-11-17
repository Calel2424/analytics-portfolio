# Python Cheat Sheet (for Data Analysis)

Focused reference for Python + pandas for analytics work.

---

## Basic Python

```python
x = 5
name = "Thomas"
numbers = [1, 2, 3]
is_active = True
```

---

## Importing Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Reading Data

```python
df = pd.read_csv("data.csv")
df = pd.read_excel("file.xlsx", sheet_name="Sheet1")
```

---

## Quick Inspection

```python
df.head()        # first 5 rows
df.tail()        # last 5 rows
df.info()        # data types + nulls
df.describe()    # summary stats
df.columns       # column names
df.shape         # (rows, columns)
```

---

## Selecting Columns & Rows

```python
df['col']                   # single column
df[['col1', 'col2']]        # multiple columns

df.iloc[0]                  # first row (by position)
df.iloc[0:5]                # first 5 rows
df.loc[0]                   # row with index 0
df.loc[df['city'] == "Paris"]
```

---

## Filtering Data

```python
df[df['amount'] > 100]

df[(df['amount'] > 100) & (df['city'] == "Paris")]

df[df['category'].isin(['A', 'B'])]
```

---

## Creating & Modifying Columns

```python
df['total'] = df['price'] * df['quantity']

df['name_clean'] = df['name'].str.strip()
df['city_lower'] = df['city'].str.lower()

df['has_discount'] = df['discount'].notna()
```

---

## Handling Missing Data

```python
df.isna().sum()                 # count nulls

df_clean = df.dropna()          # drop rows with any nulls

df_filled = df.fillna(0)        # fill nulls with 0

df_filled = df.fillna({
    'city': 'Unknown',
    'amount': 0
})
```

---

## Removing Duplicates

```python
df_no_dupes = df.drop_duplicates()

df_no_dupes = df.drop_duplicates(subset=['id'])
```

---

## Grouping & Aggregation

```python
df_grouped = (
    df.groupby('region')['amount']
      .sum()
      .reset_index()
)

df_multi = (
    df.groupby('region').agg(
        total_amount=('amount', 'sum'),
        avg_amount=('amount', 'mean'),
        row_count=('amount', 'count')
    ).reset_index()
)
```

---

## Merging DataFrames

```python
merged = pd.merge(df1, df2, on='id', how='left')
```

---

## Sorting

```python
df_sorted = df.sort_values(by='amount', ascending=False)

df_sorted = df.sort_values(by=['region', 'amount'],
                           ascending=[True, False])
```

---

## Basic Plotting

```python
df['amount'].plot(kind='hist')
plt.show()

df.plot(x='date', y='sales', kind='line')
plt.show()
```

---

## Useful Notebook Tips

- Run cell: Shift + Enter  
- Add new cell above/below: A / B (in command mode)  
- Use markdown cells for notes and structure  
