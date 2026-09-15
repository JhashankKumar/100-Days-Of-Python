# Public, Protected, and Private Variables in Python

In Python, **public, protected, and private variables** are used to indicate how class attributes are intended to be accessed.

Unlike languages such as Java or C++, Python does not strictly enforce access modifiers. Instead, Python mainly uses **naming conventions** and **name mangling**.

---

## 1. Public Variables

A variable without an underscore is considered **public**.

Public variables can be accessed and modified directly from outside the class.

### Example

```python
class User:
    def __init__(self):
        self.name = "Jhashank"
        self.age = 25


user = User()

print(user.name)
print(user.age)
```

### Output

```text
Jhashank
25
```

You can also modify the variable directly:

```python
user.name = "John"

print(user.name)
```

### Convention

```python
self.name
```

**Meaning:** The variable is part of the class's public interface and can normally be accessed directly.

---

## 2. Protected Variables

A variable starting with a **single underscore (`_`)** is considered **protected** by convention.

```python
class User:
    def __init__(self):
        self.name = "Jhashank"
        self._age = 25
```

The single underscore means:

> This variable is intended for internal use and should generally not be accessed directly from outside the class.

However, Python **does not prevent access** to protected variables.

### Example

```python
user = User()

print(user._age)
```

### Output

```text
25
```

So this is allowed, but it is generally discouraged.

### Protected variables in inheritance

Protected variables can be accessed by subclasses.

```python
class User:
    def __init__(self):
        self._age = 25


class Employee(User):
    def show_age(self):
        print(self._age)


employee = Employee()

employee.show_age()
```

### Output

```text
25
```

### Convention

```python
self._age
```

**Meaning:** The variable is intended to be used internally and can be accessed by subclasses.

---

## 3. Private Variables

A variable starting with **two underscores (`__`)** is considered private.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 10000
```

Direct access from outside the class will fail:

```python
account = BankAccount()

print(account.__balance)
```

### Output

```text
AttributeError
```

However, Python does not provide true private variables.

Instead, Python uses a mechanism called **name mangling**.

The variable:

```python
__balance
```

is internally changed approximately to:

```python
_BankAccount__balance
```

Therefore, this technically works:

```python
print(account._BankAccount__balance)
```

### Output

```text
10000
```

However, accessing it this way is **not recommended**.

---

# Public vs Protected vs Private

| Type      | Syntax   | Direct Outside Access | Subclass Access  | Purpose                                 |
| --------- | -------- | --------------------- | ---------------- | --------------------------------------- |
| Public    | `name`   | Yes                   | Yes              | Public interface                        |
| Protected | `_name`  | Yes, but discouraged  | Yes              | Internal/subclass use                   |
| Private   | `__name` | No direct access      | No direct access | Name mangling / avoid accidental access |

---

# Example Using All Three

```python
class BankAccount:

    def __init__(self):
        self.owner = "Jhashank"          # Public
        self._account_type = "Savings"   # Protected
        self.__balance = 10000           # Private

    def get_balance(self):
        return self.__balance


account = BankAccount()

print(account.owner)          # Public
print(account._account_type)  # Protected
print(account.get_balance())  # Private accessed through method
```

### Output

```text
Jhashank
Savings
10000
```

---

# Encapsulation Example

Private variables are commonly used to support **encapsulation**.

For example, consider a bank account.

Instead of allowing users to directly modify the balance, we can control how the balance changes.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Now:

```python
account = BankAccount(10000)

account.deposit(500)

print(account.get_balance())
```

### Output

```text
10500
```

The balance is controlled through the `deposit()` method.

This prevents invalid operations such as:

```python
account.__balance = -50000
```

---

# Important Python Concept

Python generally follows the philosophy:

> **"We're all consenting adults here."**

Python relies more on **developer conventions** than strict access restrictions.

Therefore:

```text
name       → Public
_name      → Protected / Internal
__name     → Private / Name Mangling
```

## Interview Tip

Do **not** say:

> "`_variable` cannot be accessed outside the class."

This is incorrect.

A protected variable **can be accessed**:

```python
object._variable
```

The underscore simply communicates:

> **"This is intended for internal use; access it directly only if you know what you're doing."**

Similarly, `__variable` is not truly private. Python uses **name mangling** to reduce accidental access and name collisions.
