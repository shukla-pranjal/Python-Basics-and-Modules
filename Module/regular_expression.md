# Regular Expressions (`re` module)


## Core Methods

| Method | Description | Example / Return Value |
| :--- | :--- | :--- |
| `re.search(pattern, text)` | Finds the **first** occurrence of a pattern. | Returns `<re.Match>` object or `None` |
| `re.finditer(pattern, text)` | Finds **all** occurrences of a pattern. | Returns an iterator yielding `<re.Match>` objects |
| `re.findall(pattern, text)` | Returns a list of all matches as strings or tuples. | `re.findall(r'\d+', '1 2 3')` -> `['1', '2', '3']` |
| `re.match(pattern, text)` | Checks for a match only at the **beginning** of the string. | `re.match(r'(.*)', text).groups()` -> `('text',)` |
| `re.sub(pattern, replacement, text)` | Replaces occurrences of the pattern with a replacement string. | `re.sub(r'apple', 'orange', text)` |

## Match Object Attributes & Methods

When a pattern is found, a Match object is returned with useful methods (all above functions):

- `match.span()`: Returns a tuple `(start, end)` with match positions.
- `match.group()`: Returns the actual matched string.
- `match.groups()`: Returns a tuple of all captured groups in the match.
- `match.string`: Returns the original string passed into the function.

---

## Metacharacters
Special characters that affect how the pattern is matched.

| Character | Description | Example Pattern | Matches |
| :---: | :--- | :--- | :--- |
| `.` | Any character (except newline) | `"he..o"` | `hello`, `hexxo` |
| `^` | Starts with | `"^hello"` | `hello world` |
| `$` | Ends with | `"planet$"` | `earth is a planet` |
| `*` | Zero or more occurrences | `"he.*o"` | `ho`, `heo`, `hello` |
| `+` | One or more occurrences | `"he.+o"` | `heo`, `hello` (Not `ho`) |
| `?` | Zero or one occurrences | `"he.?o"` | `heo`, `helo` (Not `hello`) |
| `{n}` | Exactly `n` occurrences | `"he.{2}o"` | `hello` |
| `\|` | Either or | `"falls\|stays"`| `falls`, `stays` |
| `()` | Capture and group | `(a\|b)` | Groups patterns together |
| `[]` | A set of characters | `[a-m]` | Any char between `a` and `m` |
| `\` | Escapes special chars or signals special sequences | `\d` | A digit |

---

## Special Sequences
Pre-defined character classes, signaled by a backslash `\`. Prefix patterns with `r` (raw string) to prevent Python from escaping backslashes (e.g., `r"\bword\b"`).

| Sequence | Description | Example |
| :---: | :--- | :--- |
| `\d` / `\D` | **Contains** digits (0-9) / Does **NOT contain** digits | `\d` |
| `\w` / `\W` | **Contains** word chars (a-Z, 0-9, `_`) / Does **NOT contain** word chars | `\w` |
| `\s` / `\S` | **Contains** whitespace / Does **NOT contain** whitespace | `\s` |
| `\b` | Match is at the **beginning or end** of a word | `r"\bain"` or `r"ain\b"` |
| `\B` | Match is present, but **NOT** at the beginning/end of a word | `r"\Bain"` or `r"ain\B"` |
| `\A` / `\Z` | Match is at the **beginning** of string / **End** of string | `\AThe` / `end\Z` |

---

## Character Sets `[]`
Specify a set of characters to match. In sets, special characters (`+`, `*`, `.`, `|`, `()`, `$`, `{}`) lose their special meaning and are treated as literal characters.

| Set | Description |
| :--- | :--- |
| `[arn]` | Any of the specified characters (`a`, `r`, or `n`) |
| `[^arn]` | Any character **EXCEPT** `a`, `r`, or `n` |
| `[a-n]` | Any lowercase character alphabetically between `a` and `n` |
| `[a-zA-Z]` | Any alphabetical character, lowercase OR uppercase |
| `[0-9]` | Any digit between `0` and `9` |
| `[0-5][0-9]` | Any two-digit number between `00` and `59` |
| `[+]` | A literal `+` character |

---

## Quick Example
```python
import re

text = "In 2023, the Cyclone hit the coast."
pattern = r"[A-Z]+yclone"

# Find first occurrence
match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' at {match.span()}") 
    # Output: Found 'Cyclone' at (13, 20)

# Iterate over all occurrences
for item in re.finditer(pattern, text):
    print(item.span())

# Using findall (Email Example)
emails = "john@gmail.com alice@yahoo.in"
pattern_email = r"([a-zA-Z0-9_.]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)"
print(re.findall(pattern_email, emails))
# Output: [('john', 'gmail', 'com'), ('alice', 'yahoo', 'in')]
```
