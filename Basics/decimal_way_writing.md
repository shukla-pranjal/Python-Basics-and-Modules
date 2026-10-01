

# 1. Round to `n` Decimal Places

```python
round(x,     2)
```

```python
round(12.567, 2)   # 12.57
round(12.5, 2)     # 12.5
```

---

# 2. Fixed Decimal Formatting

```python
f"{x:.2f}"
```

```python
x = 12.5
print(f"{x:.2f}")   # 12.50
```

---

# 3. Remove Trailing Zeros

```python
f"{x:.2f}".rstrip('0').rstrip('.')
```

```python
12.50 → 12.5
10.00 → 10
8.75  → 8.75
```

---

# 4. Integer Formatting with Leading Zeros

```python
f"{x:04d}"
```

```python
x = 25
print(f"{x:04d}")   # 0025
```

---

# 5. Comma Separator

```python
f"{x:,}"
```

```python
1234567 → 1,234,567
```

---

# 6. Binary, Octal, Hex

```python
bin(x)      # '0b1010'
oct(x)      # '0o12'
hex(x)      # '0xa'
```

Without prefixes:

```python
format(x, 'b')
format(x, 'o')
format(x, 'x')
```

---

# 7. Percentage

```python
f"{x:.2%}"
```

```python
x = 0.2567
print(f"{x:.2%}")   # 25.67%
```

---

# 8. Scientific Notation

```python
f"{x:.2e}"
```

```python
12345 → 1.23e+04
```

---

# 9. Left, Right, Center Alignment

```python
f"{name:<10}"   # left
f"{name:>10}"   # right
f"{name:^10}"   # center
```

---

# 10. String Repetition

```python
"-" * 20
```

---

# 11. Fast Input

```python
import sys
input = sys.stdin.readline
```

---

# 12. Read List of Integers

```python
arr = list(map(int, input().split()))
```

---

# 13. Read Multiple Variables

```python
a, b, c = map(int, input().split())
```

---

# 14. Swap Variables

```python
a, b = b, a
```

---

# 15. Ternary Operator

```python
ans = "Even" if n % 2 == 0 else "Odd"
grade = "A" if score > 90 else "B" if score > 80 else "C"
```

---


# 17. Sort with Key

```python
arr.sort(key=len)
arr.sort(key=lambda x: x[1])
```

---

# 18. Reverse List

```python
arr[::-1]
```

---

# 19. Frequency Count

```python
from collections import Counter
freq = Counter(arr)
```

---

# 20. Default Dictionary

```python
from collections import defaultdict
mp = defaultdict(int)
```

---

# 21. Join Strings

```python
print(" ".join(map(str, arr)))
```

---

# 22. ASCII Conversion

```python
ord('A')   # 65
chr(65)    # 'A'
```

---

# 23. Infinity

```python
INF = float('inf')
```

---

# 24. Ceiling Division

```python
(a + b - 1) // b
```

---

# 25. Check All / Any

```python
all(x > 0 for x in arr)
any(x < 0 for x in arr)
```

---

# 26. Unique Elements

```python
list(set(arr))
```

---

# 27. Zip

```python
for a, b in zip(arr1, arr2):
    print(a, b)
```

---

# 28. Unzip

```python
a, b = zip(*pairs)
```

---

# 29. Max with Key

```python
max(strings, key=len)
```

---

# 30. Lambda Functions

```python
square = lambda x: x * x
```

---

# 31. Safe Index Search

```python
idx = arr.index(x) if x in arr else -1
```

---

# 32. Slicing Tricks

```python
arr[:k]
arr[k:]
arr[::-1]
```

---

# 33. Matrix Input

```python
mat = [list(map(int, input().split())) for _ in range(n)]
```

---

# 34. Flatten Matrix

```python
flat = [x for row in mat for x in row]
```

---

# 35. Most Useful Float Formatter

```python
def fmt(x):
    return f"{x:.2f}".rstrip('0').rstrip('.')
```
