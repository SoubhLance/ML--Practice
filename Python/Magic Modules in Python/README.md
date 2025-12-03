# 📘 Python Dunder (Magic) Methods

Dunder methods (short for "**Double UNDERSCORE**") are special methods in Python that start and end with `__`. They let your classes behave like built-in types (lists, dicts, numbers, functions, etc). This guide explains the most important ones with simple examples.

---

## 1. Object Construction

### `__init__(self, ...)`
Called after the object is created. Used to initialize attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### `__new__(cls, ...)`
Called before the object is created. Rarely used (mainly for immutable types or singletons).

---

## 2. String Representation

### `__str__(self)`
Defines what you see when you `print()` the object. User-friendly.

```python
def __str__(self):
    return f"{self.name} is {self.age} years old"
```

### `__repr__(self)`
Developer-friendly representation. Should look like valid Python code.

```python
def __repr__(self):
    return f"Student({self.name!r}, {self.age!r})"
```

---

## 3. Length, Size, Truthiness

### `__len__(self)`
Lets your object work with `len(obj)`.

```python
def __len__(self):
    return len(self.items)
```

### `__bool__(self)`
Controls truthiness when using `if obj:`.

```python
def __bool__(self):
    return self.age > 0
```

---

## 4. Indexing & Assignment — Make Objects Behave Like Lists

### `__getitem__(self, index)`
Allows indexing: `obj[index]`

```python
def __getitem__(self, index):
    return self.items[index]
```

### `__setitem__(self, index, value)`
Allows assignment: `obj[index] = value`

```python
def __setitem__(self, index, value):
    self.items[index] = value
```

### `__delitem__(self, index)`
Allows deletion: `del obj[index]`

```python
def __delitem__(self, index):
    del self.items[index]
```

### `__contains__(self, item)`
Supports the `in` keyword: `item in obj`

```python
def __contains__(self, item):
    return item in self.items
```

---

## 5. Iteration

### `__iter__(self)`
Makes the object iterable (usable in `for` loops).

```python
def __iter__(self):
    return iter(self.items)
```

### `__next__(self)`
Used for manual iterator implementation (returns next item or raises `StopIteration`).

---

## 6. Operator Overloading

Make your class work with arithmetic operators.

### `__add__(self, other)` — `+`
```python
def __add__(self, other):
    return Vec(self.x + other.x, self.y + other.y)
```

### Other Arithmetic Operators
- `__sub__(self, other)` — `-`
- `__mul__(self, other)` — `*`
- `__truediv__(self, other)` — `/`
- `__floordiv__(self, other)` — `//`
- `__mod__(self, other)` — `%`
- `__pow__(self, other)` — `**`

---

## 7. Comparisons

### `__eq__(self, other)` — `==`
```python
def __eq__(self, other):
    return self.name == other.name
```

### Other Comparison Operators

| Method    | Operator |
|-----------|----------|
| `__lt__`  | `<`      |
| `__le__`  | `<=`     |
| `__gt__`  | `>`      |
| `__ge__`  | `>=`     |
| `__ne__`  | `!=`     |

---

## 8. Callability

### `__call__(self, ...)`
Makes the object act like a function.

```python
class Multiplier:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return x * self.n

# Usage
m = Multiplier(5)
print(m(10))  # Output: 50
```

---

## 9. Context Manager

### `__enter__(self)` & `__exit__(self, exc_type, exc_value, traceback)`
Used with `with` statements for resource management.

```python
def __enter__(self):
    print("Starting...")
    return self

def __exit__(self, exc_type, exc_value, traceback):
    print("Cleaning up...")
    return False  # Propagate exceptions

# Usage
with MyContext():
    # do something
    pass
```

---

## 10. Hashing

### `__hash__(self)`
Needed to store objects in sets or as dictionary keys. Must be immutable.

```python
def __hash__(self):
    return hash(self.name)
```

**Note:** If you define `__eq__`, you should also define `__hash__` to maintain consistency.

---

## 11. Attribute Handling

### `__getattr__(self, name)`
Called when an attribute doesn't exist.

```python
def __getattr__(self, name):
    return f"No such attribute: {name}"
```

### `__setattr__(self, name, value)`
Controls attribute assignment.

### `__delattr__(self, name)`
Controls attribute deletion.

---

## 12. Object Destruction

### `__del__(self)`
Called when the object is about to be garbage collected.

```python
def __del__(self):
    print("Object destroyed")
```

**Note:** Not guaranteed to be called immediately. Use context managers for cleanup instead.

---

## 📦 Complete Example

Here's a `Bag` class that combines many dunder methods:

```python
class Bag:
    def __init__(self, items=None):
        self.items = items or []
    
    def __str__(self):
        return f"Bag with {len(self.items)} items"
    
    def __repr__(self):
        return f"Bag({self.items!r})"
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    
    def __add__(self, other):
        return Bag(self.items + other.items)

# Usage Examples
bag = Bag(['apple', 'banana'])
print(len(bag))           # 2
print('apple' in bag)     # True
print(bag[0])             # 'apple'

for item in bag:
    print(item)

bag2 = Bag(['orange'])
bag3 = bag + bag2         # Combines bags
```

---

## 🎯 Quick Reference

| Category | Methods |
|----------|---------|
| **Construction** | `__init__`, `__new__` |
| **Representation** | `__str__`, `__repr__` |
| **Arithmetic** | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| **Comparison** | `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__` |
| **Container** | `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__` |
| **Callable** | `__call__` |
| **Context** | `__enter__`, `__exit__` |
| **Other** | `__hash__`, `__bool__`, `__del__` |

---

**Pro Tip:** You don't need to implement all dunder methods. Only add the ones that make sense for your class!