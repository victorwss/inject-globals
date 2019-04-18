# inject-globals
A function for injecting global variables into function calls.

## Usage example:

A simple usage example is this:

```python
from inject_globals import inject_globals

@inject_globals(a = "Hello", b = "World")
def hello():
    print(f"{a} {b}")

hello()
```

However, that example is somewhat silly. It's power shows up when you are creating other decorators, like this one:

```python
def run_n_times(n):
    def middle(func):
        from functools import wraps

        @wraps(func)
        def inner(*args, **kwargs):
            r = []
            for i in range(1, n + 1):
                r.append(inject_globals(it = i)(func)(*args, **kwargs))
            return r
        return inner
    return middle

@run_n_times(3)
def foo():
    return f"This is the iteration #{it}."

assert foo() == ["This is the iteration #1.", "This is the iteration #2.", "This is the iteration #3."]
```