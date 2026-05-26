# NumPy Module (`numpy`)

NumPy (Numerical Python) is a core library for fast, memory-efficient multi-dimensional arrays and mathematical operations. It is written in C, making it significantly faster and less memory-intensive than standard Python lists.

## Array Creation & Initialization

| Method | Description | Example |
| :--- | :--- | :--- |
| `np.array(list)` | Creates a NumPy array from a Python list or tuple. | `np.array([1, 2, 3]) -> array([1. , 2.33, 3.67, 5. ])` |
| `np.arange(start, stop, step)` | Creates an array with evenly spaced values. | `np.arange(0, 10, 2)` → `[0, 2, 4, 6, 8]` |
| `np.linspace(start, stop, num)` | Creates an array with `num` linearly spaced values. | `np.linspace(1, 5, 4)` |
| `np.logspace(start, stop, num)` | Creates an array with `num` logarithmically spaced values. | `np.logspace(1, 3, 3)` → `[10, 100, 1000]` |
| `np.empty(shape)` | Creates an uninitialized (random values) array. | `np.empty((4, 6))` |
| `np.empty_like(array)` | Creates an empty array with the same shape as `array`. | `np.empty_like(myarr)` |
| `np.identity(n)` | Creates an `n x n` identity matrix. | `np.identity(3)` |
| `np.eye(R, C, k)` | Similar to identity, but allows shifting the diagonal. | `np.eye(4)` |
| `np.zeros(shape)` | Creates an array filled with zeros. | `np.zeros((2, 2))` |
| `np.ones(shape)` | Creates an array filled with ones. | `np.ones((2, 3))` |
| `np.full(shape, val)` | Creates an array filled with a specific value. | `np.full((2, 3), 5)` |
| `np.random.rand(shape)` | Fills array with random floats in range `[0, 1)`. | `np.random.rand(3, 3)` |
| `np.random.randint(start, end, shape)` | Fills array with random integers in `[start, end)`. | `np.random.randint(0, 10, (2, 2))` |

---

## Array Attributes

If `arr` is a NumPy array:

- `arr.shape`: Returns a tuple of the array's dimensions (e.g., `(2, 3)`).
- `arr.ndim`: Returns the number of dimensions (axes).
- `arr.size`: Returns the total number of elements.
- `arr.nbytes`: Returns the total bytes consumed by the elements.
- `arr.itemsize`: Returns the length of one array element in bytes.
- `arr.dtype`: Returns the data type of the elements.

---

## Restructuring & Reshaping

| Method | Description |
| :--- | :--- |
| `arr.reshape(shape)` | Reshapes the array to the new shape. Use `arr.reshape(-1)` to flatten or infer a dimension automatically. |
| `arr.ravel()` | Flattens the array into a 1D array. |
| `arr.flatten()` | Returns a 1D copy of the array. |
| `arr.T` or `arr.transpose()` | Returns the transpose of the matrix. |
| `arr.flat` | Returns a 1D iterator over the array elements. |
| `np.flip(arr, axis)` | Reverses the elements along the specified axis. |
| `np.insert(arr, obj, val, axis)` | Inserts values into `arr` before index `obj` along `axis`. |
| `arr.tolist()` | Converts the NumPy array back into a standard Python list. |

---

## Axes in NumPy
Many multidimensional operations accept an `axis` argument:
- `axis=0`: Operations act vertically (down columns / across rows).
- `axis=1`: Operations act horizontally (across columns / down rows).

---

## Mathematical & Aggregate Operations

Operations like `+`, `-`, `*`, `/` work element-wise on arrays of matching shapes. Matrix multiplication requires matching inner dimensions.

| Method | Description |
| :--- | :--- |
| `np.add(a, b)` / `a + b` | Element-wise addition. |
| `np.subtract(a, b)` / `a - b` | Element-wise subtraction. |
| `np.multiply(a, b)` / `a * b` | Element-wise multiplication. |
| `np.divide(a, b)` / `a / b` | Element-wise division. |
| `np.sqrt(arr)` | Returns the square root of each element. |
| `np.exp(arr)` | Returns the exponential (`e^x`) of each element. |
| `arr.sum(axis)` | Returns the sum of elements (optionally along an axis). |
| `arr.max(axis)` | Returns the maximum element. |
| `arr.min(axis)` | Returns the minimum element. |

---

## Searching, Sorting, & Filtering

| Method | Description |
| :--- | :--- |
| `arr.argmax(axis)` | Returns the **index** of the maximum element. |
| `arr.argmin(axis)` | Returns the **index** of the minimum element. |
| `arr.argsort(axis)` | Returns an array of **indices** that would sort the array. <br> Example: `np.array([3, 1, 2]).argsort()` → `[1, 2, 0]` |
| `np.where(condition, x, y)` | Returns elements from `x` if condition is true, else from `y`. <br> Example: `np.where(arr < 20, arr, arr + 5)` |
| `np.count_nonzero(arr)` | Returns the count of non-zero elements in the array. |
| `np.intersect1d(arr1, arr2)` | Returns the sorted, unique values that are in both input arrays. |

---

## Common Data Types (`dtype`)
NumPy supports many data types. Specify during creation: `np.array([1, 2], dtype=np.int64)`.

| Code | Type | Description |
| :--- | :--- | :--- |
| `i` | Integer | `int8`, `int16`, `int32`, `int64` |
| `u` | Unsigned Int | `uint8`, `uint16`, `uint32`, `uint64` |
| `f` | Float | `float16`, `float32`, `float64` |
| `c` | Complex | `complex64`, `complex128` |
| `b` | Boolean | `bool_` |
| `O` | Object | Python objects |
| `U` | Unicode | Unicode Strings |

---

## Indexing, Slicing & `np.where`

### Slicing (works same as Python lists)
```python
arr[::-1]        # reverse 1D array
arr[:, ::-1]     # reverse each row of a 2D array
```

### `np.where(condition, x, y)`
Returns elements from `x` where condition is True, else from `y`.
```python
arr = np.where(condition, true_val, false_val)
```

### `np.indices(shape)`
Returns an open mesh of index arrays for a given shape — useful for
building coordinate-based arrays without explicit loops.
```python
i, j = np.indices((n, n))   # i = row indices, j = col indices
```

---

## Patterns & Recipes

### Checkerboard Pattern (two methods)

**Method 1 – `np.where` + `np.indices`:**
```python
import numpy as np
n = 8
i, j = np.indices((n, n))
arr = np.where((i + j) % 2 != 0, 1, 0)
```

**Method 2 – Slice assignment:**
```python
x = np.zeros((n, n), dtype=int)
x[1::2, ::2] = 1    # odd rows, even cols
x[::2, 1::2] = 1    # even rows, odd cols
print(x)
# [[0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  ...]
```

### Advanced 2D Input from stdin
```python
arr = np.array([list(map(int, input().split())) for _ in range(rows)])
```

---

## Linear Algebra (`np.linalg`)

| Method | Description |
| :--- | :--- |
| `np.linalg.det(arr)` | Returns the determinant of a square matrix. |

