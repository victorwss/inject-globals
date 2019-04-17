from functools import wraps

def inject_globals(__do_not_use_this_parameter = None, **globals):
    """Decorator that inject the given variables as global variable to the decorated function.

    Keyword arguments:
    __do_not_use_this_parameter -- sentinel to guard against bad usage.
    **globals -- the globals variables that will be injected into the decorated funcion call.

    Example usage:

    @inject_globals(a = "Hello", b = "World")
    def hello():
        print(f"{a} {b}")

    hello() # Shows "Hello World"

    Bad usage example:

    @inject_globals(42) # Don't do this!
    def hello():
        print("Hello")

    """
    def middle(func):
        @wraps(func)
        def inner(*args2, **kwargs):
            sentinel = object()
            olds = {}
            g = func.__globals__
            for k in globals:
                olds[k] = g.get(k, sentinel)
                g[k] = globals[k]
            try:
                return func(*args2, **kwargs)
            finally:
                for k in olds:
                    old = olds[k]
                    if old is sentinel:
                        del g[k]
                    else:
                        g[k] = old
        return inner
    if __do_not_use_this_parameter == None:
        return middle
    if callable(__do_not_use_this_parameter):
        return middle(__do_not_use_this_parameter)
    raise Exception("Bad usage for inject_globals")