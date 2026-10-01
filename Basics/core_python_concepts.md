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

## 4. Dictionaries (`dict`)
Stores **key-value pairs**.
```python
d = {"a": 1, "b": 2}
```

### Important Methods
| Method       | Description         |
| ------------ | ------------------- |
| `d.keys()`   | Returns all keys    |
| `d.values()` | Returns all values  |
| `d.items()`  | Returns key-value pairs |
| `d.get(key)` | Safe access (returns None if not found) |
| `d.update()` | Add/update multiple key-value pairs |
| `d.pop(key)` | Remove key and return its value |
| `d.popitem()`| Removes and returns the **last inserted** key-value pair as a tuple. |
| `d.clear()`  | Remove all items    |
| `d.copy()`   | Returns a shallow copy |

### Common Operations & Looping
```python
d["c"] = 3          # Add a new pair
d["a"] = 10         # Update an existing pair
print(d["a"])       # Access value
print("a" in d)     # Check if key exists

# Looping through a dictionary
for k, v in d.items():
    print(k, v)
```

### Dictionary Tricks & Patterns
**Duplicate Keys:** When duplicate keys are encountered during dictionary creation or assignment, the **last assignment wins**.

**Frequency Counter Pattern:**
```python
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

**`setdefault()` Method:**
```python
di.setdefault(key, default_value)
```
- If the `key` already exists, it returns the existing value.
- If the `key` does not exist, it creates it with `default_value` and returns the `default_value`.

**Creating a Dictionary using `zip()`:**
```python
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))  # {'a': 1, 'b': 2}
```


## 5. Sets (`set`)
Stores **unique elements**. Duplicates are automatically removed.
```python
s = {1, 2, 3}
```

### Important Methods & Operations
| Method / Operator | Description |
| ----------------- | ----------- |
| `add(x)`          | Add element |
| `remove(x)`       | Remove element (throws error if absent) |
| `discard(x)`      | Remove safely (no error if absent) |
| `pop()`           | Remove and return a random element |
| `clear()`         | Empty the set |
| `a \| b` (union)  | Combine elements from both sets |
| `a & b` (intersection) | Elements common to both sets |
| `a - b` (difference) | Subtract elements in b from a |
| `a ^ b` (symmetric difference) | Elements present in either set but not in both |

### Removing Duplicates from a List
```python
arr = list(set(arr))
```

### Subset and Superset Comparison (`<`, `<=`)
Python supports subset/superset operators.
- **Sets:** The `<` operator checks for **proper subsets**.
  ```python
  s1 = {1, 2}
  s2 = {1, 2, 3}
  print(s1 < s2)  # True, s1 is a proper subset of s2
  print(s1 <= s1) # True, s1 is a subset of itself
  ```

## 6. Tuples
Tuples are immutable. The `<` operator performs **lexicographical (element-by-element)** comparison.
```python
t1 = (1, 2, 4, 3)
t2 = (1, 2, 3, 4)
print(t1 < t2)  # False, because t1[2] (4) > t2[2] (3)
```

## 7. Sorting (`sorted()` vs `.sort()`)

| Function   | Changes Original? | Works on |
| ---------- | ----------------- | -------- |
| `sorted()` | No (Returns new list) | Any iterable (list, tuple, dict, set, string) |
| `.sort()`  | Yes (In-place)    | Only Lists |

### Using `sorted()`
Syntax: `sorted(iterable, key=..., reverse=False)`

**1. Sorting a String**
```python
s = "cab"
sorted_s = sorted(s)        # ['a', 'b', 'c']
joined_s = "".join(sorted_s) # "abc"
```

**2. Sorting a Dictionary**
```python
d = {"c": 3, "a": 1, "b": 2}

# By default sorts keys
sorted(d)  # ['a', 'b', 'c']

# Sort by Keys
sorted(d.items(), key=lambda x: x[0])  # [('a', 1), ('b', 2), ('c', 3)]

# Sort by Values
sorted(d.items(), key=lambda x: x[1])  # [('a', 1), ('b', 2), ('c', 3)]
```

**3. Sorting by Multiple Conditions**
```python
arr = [("banana", 2), ("apple", 5), ("apple", 2)]
# Sort by first element ascending, then second element descending
arr.sort(key=lambda x: (x[0], -x[1]))
```

**4. Common CP/Interview Tricks**
```python
words = ["apple", "kiwi", "banana"]

# Sort by length
sorted(words, key=len)

# Sort ignoring case
sorted(words, key=str.lower)
```

## 8. Data Structure Differences

| Type    | Ordered     | Mutable | Duplicates  |
| ------- | ----------- | ------- | ----------- |
| `list`  | Yes         | Yes     | Yes         |
| `tuple` | Yes         | No      | Yes         |
| `set`   | No          | Yes     | No          |
| `dict`  | Key ordered | Yes     | Keys unique |
