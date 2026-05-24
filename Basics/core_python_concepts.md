# Core Python Concepts & Data Structures

## 1. Conditional Statements
- `if` / `elif` / `else` are the standard conditional statements in Python.
- **Note:** Python does **not** have a traditional `switch` statement (though Python 3.10+ introduced `match`/`case`).

## 2. Strings
### Representation Formatting (`!s` vs `!r`)
```python
text = "hello\nworld"
print(f"{text!s}")  # Uses str() -> processes the newline
print(f"{text!r}")  # Uses repr() -> raw representation ('hello\nworld')
```

### Concatenation Errors
```python
# TypeError: can only concatenate str (not "int") to str
print("hello" + 1 + 2 + 3) 
```
Unlike JavaScript, Python does not automatically coerce integers to strings during concatenation.

## 3. Lists
### Finding the Index of the Maximum Element
```python
ls = [10, 50, 20, 30]
max_index = ls.index(max(ls))
```

## 4. Dictionaries
### Duplicate Keys
When duplicate keys are encountered during dictionary creation or assignment, the **last assignment wins**.

### `setdefault()` Method
```python
di.setdefault(key, default_value)
```
- If the `key` already exists, it returns the existing value.
- If the `key` does not exist, it creates it with `default_value` and returns the `default_value`.

### `popitem()` Method
Removes and returns the **last inserted** key-value pair as a tuple.
```python
di = {'Name': 'Pranjal', 'Age': 19, 'Subject': 'Python'}
item = di.popitem()
print(item)  # ('Subject', 'Python')
print(di)    # {'Name': 'Pranjal', 'Age': 19}
```

## 5. Sets & Tuples
### Subset and Superset Comparison (`<`, `<=`)
Python supports subset/superset operators.

- **Tuples:** The `<` operator performs **lexicographical (element-by-element)** comparison.
  ```python
  t1 = (1, 2, 4, 3)
  t2 = (1, 2, 3, 4)
  print(t1 < t2)  # False, because t1[2] (4) > t2[2] (3)
  ```
- **Sets:** The `<` operator checks for **proper subsets**.
  ```python
  s1 = {1, 2}
  s2 = {1, 2, 3}
  print(s1 < s2)  # True, s1 is a proper subset of s2
  print(s1 <= s1) # True, s1 is a subset of itself
  ```
