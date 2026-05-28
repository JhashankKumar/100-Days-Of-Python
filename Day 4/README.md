# Python Collections (Arrays) Mind Map

```text
Python Collections
│
├── List []
│   │
│   ├── Ordered → Yes
│   ├── Changeable → Yes
│   ├── Duplicates Allowed → Yes
│   ├── Indexed → Yes
│   │
│   ├── Syntax
│   │     my_list = [1, 2, 3]
│   │
│   ├── Common Methods
│   │     append()
│   │     insert()
│   │     remove()
│   │     pop()
│   │     sort()
│   │
│   └── Use Case
│         Store multiple items that may change
│
├── Tuple ()
│   │
│   ├── Ordered → Yes
│   ├── Changeable → No
│   ├── Duplicates Allowed → Yes
│   ├── Indexed → Yes
│   │
│   ├── Syntax
│   │     my_tuple = (1, 2, 3)
│   │
│   ├── Common Methods
│   │     count()
│   │     index()
│   │
│   └── Use Case
│         Fixed data that should not change
│
├── Set {}
│   │
│   ├── Ordered → No
│   ├── Changeable → Yes*
│   ├── Duplicates Allowed → No
│   ├── Indexed → No
│   │
│   ├── Syntax
│   │     my_set = {1, 2, 3}
│   │
│   ├── Common Methods
│   │     add()
│   │     remove()
│   │     union()
│   │     intersection()
│   │
│   └── Use Case
│         Store unique values
│
└── Dictionary {}
    │
    ├── Ordered → Yes
    ├── Changeable → Yes
    ├── Duplicates Allowed → No Keys
    ├── Indexed → Accessed by Keys
    │
    ├── Syntax
    │     my_dict = {
    │         "name": "John",
    │         "age": 25
    │     }
    │
    ├── Common Methods
    │     keys()
    │     values()
    │     items()
    │     update()
    │     pop()
    │
    └── Use Case
          Store data in key-value pairs
```

---

# Quick Comparison Table

| Collection | Ordered | Changeable | Duplicates       | Indexed   |
| ---------- | ------- | ---------- | ---------------- | --------- |
| List       | ✅ Yes   | ✅ Yes      | ✅ Yes            | ✅ Yes     |
| Tuple      | ✅ Yes   | ❌ No       | ✅ Yes            | ✅ Yes     |
| Set        | ❌ No    | ✅ Yes*     | ❌ No             | ❌ No      |
| Dictionary | ✅ Yes   | ✅ Yes      | ❌ Duplicate Keys | ✅ By Keys |

---

# Easy Memory Trick

* **List** → "Shopping List" → can change anytime
* **Tuple** → "Fixed Data" → cannot change
* **Set** → "Unique Items" → no duplicates
* **Dictionary** → "Word Meaning" → key : value pairs

---

# Example Code

```python
# List
fruits = ["apple", "banana", "apple"]

# Tuple
coordinates = (10, 20)

# Set
unique_numbers = {1, 2, 3}

# Dictionary
student = {
    "name": "John",
    "age": 21
}
```
