from inject_globals import inject_globals

def test_decoration():
    @inject_globals(a = "Hello", b = "World")
    def hello(c):
        return f"{a} {b} {c}"

    assert hello("Great") == "Hello World Great"

def test_ill_decoration_1():
    @inject_globals()
    def hello2():
        return "ok"

    assert hello2() == "ok"

def test_ill_decoration_2():
    @inject_globals
    def hello3():
        return "ok"

    assert hello3() == "ok"

def test_ill_decoration_3():
    try:
        @inject_globals(42)
        def hello4():
            assert False
    except Exception as x:
        assert str(x) == "Bad usage for inject_globals"

def test_for_decorator():
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