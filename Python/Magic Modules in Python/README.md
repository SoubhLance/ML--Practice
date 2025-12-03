## 📘 Python Dunder (Magic) Methods

- Dunder methods (short for “Double UNDERSCORE”) are special methods in Python that start and end with `__`.
They let your classes behave like built-ins (lists, dicts, numbers, functions, etc).
This guide explains the most important ones with simple examples.

1. Object Construction — `__init__` & `__new__`
- `__init__(self, ...)`
- Called after the object is created. Used to initialize attributes.
```     
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age
```

- `__new__(cls, ...)`
- Called before the object is created. Rarely used (for immutables).