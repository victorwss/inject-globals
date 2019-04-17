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

However, that example is somewhat silly. It's power shows up when you are creating other decorators.