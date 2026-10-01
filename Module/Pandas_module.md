# Pandas Module Guide

Pandas is an open-source data analysis library written in Python. It leverages the power and speed of NumPy to make data analysis and preprocessing easy for data scientists. It provides rich and highly robust data operations, especially for tabular data (like CSVs).

## Core Data Structures

- **Series (1D)**: A single column or row of data.
  ```python
  ser = pd.Series(np.random.rand(34))
  # Type: <class 'pandas.core.series.Series'>
  ```
- **DataFrame (2D)**: A tabular spreadsheet (rows and columns).
  ```python
  df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
  # Type: <class 'pandas.core.frame.DataFrame'>
  ```

## DataFrame Creation & I/O

### Creating a DataFrame
You can create a DataFrame from a dictionary or a list of lists.
```python
dict1 = {
    "name": ['Pranjal', 'Kumar', 'Akash'],
    "marks": [92, 34, 24],
    "city": ['ran', 'del', 'kol']
}
df = pd.DataFrame(dict1)
```
- By default, columns are the dictionary keys. You can specify columns manually with `columns=['a', 'b', ...]`.

### Reading & Writing CSV
- **Read**: `pd.read_csv('file_path.csv')`
  - Use `header=None` if the file has no column names.
- **Write**: `df.to_csv('file_path.csv')`
  - Use `index=False` to prevent saving the auto-generated row indices.

## Basic Data Exploration

- `df.head(n)`: Returns the first `n` rows (default 5).
- `df.tail(n)`: Returns the last `n` rows.
- `df.describe()`: Returns statistical summaries (count, mean, std, min, 25%, 50%, 75%, max) for numeric columns.
- `df.info()`: Shows memory usage, data types, and the number of non-null objects.
- `df.shape`: Returns a tuple of `(rows, columns)`.
- `df.dtypes`: Returns the data type of each column.
- `df.columns`: Returns a list-like object of column names.
- `df.values`: Returns the DataFrame as a NumPy array format.
- `df.T`: Transposes rows and columns.

## Data Selection & Indexing

> **Note:** In pandas, index starts from 0 (2nd row in CSV context). `[]` and `loc` are primarily used, but `.loc` is recommended for good programming practice.

### Basic Selection
- Single column: `df['A']`
- Multiple columns: `df[['A', 'B']]`
- Cell value: `df['column_name'][index]`

### Using `.loc` (Label-based)
- `df.loc[row_label]`
- `df.loc[[row1, row2]]`
- `df.loc[:, 'A':'C']` (Slices columns A to C)
- Modifying a cell: `df.loc[row, column] = new_value` (Creates the row/col if it doesn't exist).

### Using `.iloc` (Index/Position-based)
Used for selecting based on 0-based integer position, even if your labels are strings.
- Slicing rows: `df.iloc[1:3]` (Selects rows 1 and 2).

### Conditional Selection & Modification
```python
# Filtering based on condition
filtered_df = df[df['COLUMN'] < any_value]

# Using loc with condition to update values
df.loc[(df["Category"] == "spam"), "Category"] = 0
```
- **`.where()`**: Replaces values where the condition is False.
  ```python
  # Keeps values > 3, replaces others with 0
  df['A'] = df['A'].where(df['A'] > 3, 0)
  ```

### Sorting
- **By Index**: `df.sort_index(axis=0, ascending=False)` (rows) or `axis=1` (columns).
- **By Values**: `df.sort_values(['column1', 'column2'])`

## Modifying the DataFrame

### Copying DataFrames
- Assignment `df1 = df2` creates a view (modifying `df1` affects `df2`).
- To make a distinct copy: `df1 = df2.copy()` or `df1 = df2[:]`.

### Renaming
- Columns (dict): `df.rename(columns={'old_col': 'new_col'}, inplace=True)`
- Replace all columns: `df.columns = ['new_col1', 'new_col2', ...]`

### Handling Indices
- Set index: `df.index = [list_of_values]`
- Reset index: `df.reset_index()`
  - By default, the old index becomes a new column (often called `index`). Use `drop=True` to prevent this.

### Dropping Rows/Columns
Use `.drop()` and set `axis` (0 for rows, 1 for columns).
```python
df.drop('column_name', axis=1, inplace=True)
df.drop(columns=['colA', 'colB'], inplace=True)
df.drop(df.columns[[0, 1, 3]], axis=1) # Drop by column index
```
> **Note:** `inplace=True` modifies the DataFrame directly without needing reassignment. It returns `None`.

### Handling Null & Duplicate Values
- **Check Nulls**: `df.isnull()` or `df['col'].isnull()` (Returns booleans). `df.notnull()` works oppositely.
- **Drop Nulls**: `df.dropna(axis=0, how='any')`
  - `how='any'`: Drops row/col if ANY value is NA.
  - `how='all'`: Drops row/col if ALL values are NA.
- **Fill Nulls**: `df.fillna(value)` (Fills `NaN` with a specific value. Can also use `method='ffill'` or `'bfill'`).
- **Drop Duplicates**: `df.drop_duplicates(subset=['col1'], keep='first')`
  - `keep` options: `'first'` (default), `'last'` (keeps last occurrence), or `False` (drops all duplicates).

### Changing Data Types
- `df.astype(new_type)` or `df['col'].astype(new_type)`

## Math, Aggregation & Grouping

### Column Statistics
- `df.mean()`: Means
- `df.median()`: Medians
- `df.std()`: Standard deviations
- `df.min()` / `df.max()`: Minimums and maximums
- `df.count()`: Count non-null values
- `df.corr()`: Compute column correlations
- **Value Counts**: `df['column'].value_counts(dropna=True)` counts unique occurrences in a column.

### GroupBy
Groups data by unique values in a column to perform aggregate math.
```python
df.groupby('column').mean()
df.groupby('column1').agg({'column2': ['mean', 'max', 'min', 'count', 'sum']})
```

## Combining DataFrames
- **Concatenate**: `pd.concat([df1, df2], ignore_index=True)`

## Reshaping
- **Pivot**: Turns unique column values into multiple columns.
  ```python
  pd.pivot(df, index="index_column", columns="col_to_spread", values="val_col")
  ```
- **Melt**: Unpivots columns back into rows (opposite of pivot).
  ```python
  pd.melt(df, id_vars="id_column", var_name="quarter", value_name="amount")
  ```
